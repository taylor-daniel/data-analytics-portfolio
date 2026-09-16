# Portfolio Workflow (with Claude)

```
1. MY WORK             finish a project, dashboard, or data fix
      ↓
2. EXPLAIN             paste notes into Claude (templates/PROJECT_INTAKE.md, or just talk)
      ↓
3. STRUCTURE           Claude identifies problem, skills, business value; asks only for real gaps
      ↓
4. PREPARE             Claude writes/updates the case study, index table, profile README
                       and writes the files into this folder on my computer
      ↓
5. SAFETY CHECK        python scripts/prepublish_check.py  +  git diff --staged
      ↓
6. REVIEW              I read everything; I decide what's accurate and safe
      ↓
7. COMMIT & PUSH       I run the git commands Claude suggests
      ↓
8. MAINTAIN            quarterly: refresh profile README, reorder featured work, retire weak items
```

## Trigger phrases

Start a message with any of these and Claude runs the full workflow:
- "I completed this project…"
- "I worked on this dashboard…"
- "I solved this data problem…"
- "Update my portfolio with…"

For each, Claude returns:
1. Skills demonstrated · business problem · business value
2. Where it belongs (new case study, addition to an existing one, or its own repo)
3. The README content (new or updated)
4. Files/folders to add
5. Confidentiality flags: what to remove or anonymise
6. GitHub topics
7. Exact `git add` / `git commit` / `git push` commands
8. Profile README update, if the work materially strengthens the portfolio

## Where does new work go?

| The work is… | Put it in |
|---|---|
| A substantial professional project | New folder in `case-studies/` |
| A new phase / dashboard / fix on an existing project | Update that case study (`docs:` or `feat:` commit) |
| A small task (one measure, one cleanup) | A bullet in the relevant case study, or nothing |
| A personal project with runnable code on public/synthetic data | Its own repo, linked from the index table |
| A learning exercise / course | Not in the portfolio unless it produces something notable |

## Rules Claude follows
- Never invents metrics, tools, responsibilities or outcomes; marks gaps with a NEEDS INPUT marker, which the pre-publish check blocks
- Separates *what I did* from *what others did*
- Anonymises by default and flags anything risky before suggesting a commit
- Doesn't create new repos for small tasks

## Maintenance cadence
- **After each project:** case study + index row + commit
- **Quarterly:** review profile README (headline, featured work, "currently" section), pin best 4–6 repos
- **Yearly:** retire or merge weaker case studies so the strongest work leads
