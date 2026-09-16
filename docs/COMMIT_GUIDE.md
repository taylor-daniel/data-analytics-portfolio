# Commit Guide

Based on [Conventional Commits](https://www.conventionalcommits.org/). Your commit history is part of your portfolio: it shows how you work.

## Format

```
<type>(<optional scope>): <what changed, imperative, lowercase, no full stop>
```

Keep the subject under ~72 characters. Add a body (blank line, then text) only when the *why* isn't obvious.

## Types

| Type | Use for | Example |
|---|---|---|
| `feat` | A new case study, dashboard, analysis, notebook or script | `feat(hr-workforce): add attrition analysis` |
| `docs` | Writing or improving README / methodology / impact text | `docs(digital-revenue): add business impact section` |
| `fix` | Correcting an error in logic, numbers or text | `fix(hr-workforce): correct tenure calculation` |
| `refactor` | Restructuring code without changing results | `refactor(pipeline): split cleaning into functions` |
| `style` | Formatting only | `style: format notebooks with black` |
| `test` | Data quality checks, unit tests | `test(pipeline): add row-count reconciliation checks` |
| `chore` | Repo housekeeping: .gitignore, folders, config | `chore: add gitignore for data files` |
| `security` | Removing or anonymising sensitive content | `security: mask system names in screenshots` |

**Scopes** = the case-study folder name, shortened (e.g. `digital-revenue`, `hr-workforce`, `profile`).

## Good vs bad

| ❌ Avoid | ✅ Instead |
|---|---|
| `updated` | `docs(hr-workforce): clarify headcount definition` |
| `final` | `feat(digital-revenue): add product traction analysis` |
| `changes` | `refactor(pipeline): replace loops with spark joins` |
| `test` | `test(pipeline): add null-key checks before join` |
| `fixed stuff` | `fix(digital-revenue): exclude cancelled quotes from premium` |

## Habits

1. **One logical change per commit.** A new case study = one `feat`; later improvements = separate `docs`/`fix` commits.
2. **Review before committing:** `git status` then `git diff --staged`.
3. **Run the confidentiality check** (`python scripts/prepublish_check.py`) before every push.
4. **Commit on `main` directly** for small documentation updates. For bigger work (a new code project), use a short-lived branch: `git switch -c feat/fabric-lakehouse`, then merge.
5. **Never "commit then delete" a secret.** Git keeps history. If something sensitive is pushed, see `SECURITY_CHECKLIST.md` → *If something leaks*.
