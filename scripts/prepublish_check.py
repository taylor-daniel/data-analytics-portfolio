#!/usr/bin/env python3
"""
Pre-publish confidentiality check for the portfolio.

Scans every file that git would commit (tracked + untracked, respecting .gitignore)
for secrets, personal data, internal URLs, risky file types and your own list of
confidential terms (.sensitive-terms.txt, which is git-ignored).

Usage (from the repo root):
    python scripts/prepublish_check.py

Exit code 0 = nothing found, 1 = review needed.
This is a safety net, not a guarantee. Always review `git diff --staged` yourself.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS_FILE = ROOT / ".sensitive-terms.txt"
SKIP_FILES = {".sensitive-terms.example.txt", "scripts/prepublish_check.py", ".gitignore"}
TEXT_EXT = {".md", ".txt", ".py", ".sql", ".ipynb", ".json", ".yml", ".yaml", ".toml",
            ".cfg", ".ini", ".dax", ".m", ".pq", ".csv", ".tsv", ".html", ".r", ".sh",
            ".ps1", ".tmdl", ".bim", ".scala", ".gitignore", ""}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg"}
RISKY_EXT = {".pbix": "Power BI file: embeds data", ".pbit": "Power BI template: check Power Query sources",
             ".xlsx": "Excel file", ".xls": "Excel file", ".xlsm": "Excel file",
             ".parquet": "data file", ".db": "database file", ".sqlite": "database file",
             ".bak": "database backup", ".pem": "key file", ".key": "key file", ".pfx": "certificate"}

PATTERNS = [
    ("Unfinished draft marker", r"\[NEEDS INPUT"),
    ("Private key", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    ("GitHub token", r"\b(ghp|gho|ghu|ghs|ghr|github_pat)_[A-Za-z0-9_]{20,}"),
    ("Databricks token", r"\bdapi[0-9a-f]{32}"),
    ("AWS access key", r"\bAKIA[0-9A-Z]{16}\b"),
    ("Azure storage key", r"AccountKey=[A-Za-z0-9+/=]{20,}"),
    ("Azure SAS token", r"[?&]sig=[A-Za-z0-9%+/=]{20,}"),
    ("JWT", r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
    ("Password / connection string", r"(?i)\b(password|pwd|passwd)\s*[=:]\s*['\"]?[^\s;'\"…\[\]]{3,}"),
    ("Hard-coded secret", r"(?i)\b(api[_-]?key|secret|token|client[_-]?secret)\s*[=:]\s*['\"][^'\"\s]{12,}['\"]"),
    ("JDBC / ODBC connection", r"(?i)\b(jdbc:[a-z]+://|Server=tcp:|Data Source=[\w.-]+)"),
    ("Databricks workspace URL", r"(?i)\b(adb-\d{6,}\.\d+|[\w-]+\.cloud)\.azuredatabricks\.net"),
    ("Azure SQL / Fabric endpoint", r"(?i)\b[\w-]+\.(database\.windows\.net|datawarehouse\.fabric\.microsoft\.com|dfs\.core\.windows\.net)"),
    ("Power BI workspace/report link", r"(?i)app\.powerbi\.com/(groups|reports)/[0-9a-f-]{20,}"),
    ("SharePoint / OneDrive URL", r"(?i)\b[\w-]+(-my)?\.sharepoint\.com"),
    ("Private IP address", r"\b(10\.\d{1,3}|192\.168|172\.(1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"),
    ("Internal hostname", r"(?i)\b[\w-]+\.(local|internal|corp|intranet)\b"),
    ("Windows user path", r"(?i)C:\\Users\\[^\\\s]+"),
    ("Email address", r"\b[A-Za-z0-9._%+-]+@(?!users\.noreply\.github\.com|example\.(com|org))[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    ("Nigerian phone number", r"(?<!\d)(\+?234|0)[789][01]\d{8}(?!\d)"),
    ("Long ID-like number (policy/NIN/BVN/account?)", r"(?<![\d.])\d{10,16}(?![\d.])"),
]


def files_to_check() -> list[Path]:
    try:
        out = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout
        return [ROOT / p for p in out.splitlines() if p.strip()]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def load_terms() -> list[str]:
    if not TERMS_FILE.exists():
        return []
    return [t.strip() for t in TERMS_FILE.read_text(encoding="utf-8", errors="ignore").splitlines()
            if t.strip() and not t.strip().startswith("#")]


def main() -> int:
    findings: list[str] = []
    images: list[str] = []
    terms = load_terms()
    compiled = [(name, re.compile(rx)) for name, rx in PATTERNS]
    term_rx = [(t, re.compile(r"(?i)\b" + re.escape(t) + r"\b")) for t in terms]

    for path in files_to_check():
        rel = path.relative_to(ROOT).as_posix()
        if rel in SKIP_FILES or not path.exists():
            continue
        ext = path.suffix.lower()
        in_sample = "/sample-data/" in f"/{rel}"

        if ext in RISKY_EXT or (ext in {".csv", ".tsv"} and not in_sample):
            findings.append(f"[FILE]   {rel}: {RISKY_EXT.get(ext, 'data file outside sample-data/')}")
        if ext in IMAGE_EXT:
            images.append(rel)
            continue
        if ext not in TEXT_EXT:
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")

        if ext == ".ipynb":
            try:
                nb = json.loads(text)
                if any(c.get("outputs") for c in nb.get("cells", [])):
                    findings.append(f"[NOTEBOOK] {rel}: has cell outputs; clear them before publishing")
            except json.JSONDecodeError:
                pass

        draft_lines = []
        for lineno, line in enumerate(text.splitlines(), 1):
            for name, rx in compiled:
                for m in rx.finditer(line):
                    if name == "Unfinished draft marker":
                        draft_lines.append(lineno)
                        break
                    findings.append(f"[{name}] {rel}:{lineno}: {m.group(0)[:60]}")
            for term, rx in term_rx:
                if rx.search(line):
                    findings.append(f"[CONFIDENTIAL TERM] {rel}:{lineno}: '{term}'")
        if draft_lines:
            findings.append(f"[DRAFT] {rel}: {len(draft_lines)} unfinished NEEDS INPUT marker(s), first at line {draft_lines[0]}")

    print("Portfolio pre-publish check")
    print("=" * 40)
    if not terms:
        print("NOTE: no .sensitive-terms.txt found. Create one (see .sensitive-terms.example.txt)")
        print("      so company, product, system and colleague names are checked too.\n")

    if findings:
        print(f"{len(findings)} item(s) need review:\n")
        for f in findings:
            print("  " + f)
    else:
        print("No automated findings.")

    if images:
        print(f"\n{len(images)} image(s) must be checked by eye (names, values, URLs, tabs, tooltips):")
        for i in images:
            print("  - " + i)

    print("\nReminder: also review `git diff --staged` before pushing.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
