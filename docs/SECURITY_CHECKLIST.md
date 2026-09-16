# Security & Confidentiality Checklist

**Rule:** if you wouldn't hand it to a competitor or put it on a billboard, it doesn't go on GitHub, public or private.

## Before every push

Run:

```bash
python scripts/prepublish_check.py
git status
git diff --staged
```

Then confirm, by eye:

### 1. Secrets
- [ ] No passwords, API keys, access tokens (e.g. Databricks `dapi…`, GitHub `ghp_…`, Azure keys)
- [ ] No connection strings (`Server=…;Password=…`, JDBC URLs)
- [ ] No `.env`, `.databrickscfg`, credential or key files

### 2. Identifying the employer
- [ ] No company, subsidiary, brand or product names → use "a financial services company", "Product A"
- [ ] No internal system names (core policy system, HRIS product + instance names) → "the transaction system", "the HRIS"
- [ ] No internal URLs: SharePoint, workspace URLs (`*.azuredatabricks.net`, `app.powerbi.com/groups/…`), server names, IPs
- [ ] No logos, email signatures, org charts

### 3. People & customers
- [ ] No employee names, IDs, emails, salaries, performance ratings, even in screenshots
- [ ] No customer names, phone numbers, emails, addresses, policy/quote numbers
- [ ] Small-group results can re-identify people ("the only female manager in Unit X") → aggregate or remove

### 4. Financial & proprietary
- [ ] No real revenue/premium figures that identify the business → use % change, indexed values, or ranges
- [ ] No internal database schemas, table names, or column names copied verbatim → rename generically
- [ ] No proprietary pricing, underwriting, or commission logic
- [ ] Code is **rewritten** to show the technique, not copied from employer repos or notebooks

### 5. Files
- [ ] No `.pbix` files built on real data (they embed the data). Screenshots of masked data only.
- [ ] No `.pbit` templates without checking Power Query for server names and credentials
- [ ] Notebooks cleared of outputs (outputs can contain real rows)
- [ ] Screenshots checked at full zoom: tooltips, filter panes, page names, file paths, browser tabs
- [ ] Image metadata stripped

### 6. Policy
- [ ] My employment contract / company policy allows describing this work publicly
- [ ] If unsure, I've generalised further or asked my manager

## Anonymisation patterns

| Real | Public version |
|---|---|
| Company name | "A [industry] company in [region]" |
| Product names | "Product A / B / C" or product category ("motor", "health") |
| ₦ / $ figures | % change, share of total, indexed to 100, or ranges |
| Employee data | Synthetic dataset with same shape |
| Table `dbo.tblPolMaster` | `policies` |
| Screenshots | Rebuild the visual on synthetic data, or blur/mask values |

## Safe data for demos
- Generate synthetic data with Python (`faker`, `numpy`) matching the real *structure*, not the real values
- Or use public datasets (Kaggle, government open data, IBM HR Attrition sample)
- Store in `sample-data/` and label it **synthetic** in the README

## Account security
- Enable **two-factor authentication** (passkey or authenticator app)
- Settings → Emails → **Keep my email address private** and **Block command line pushes that expose my email**
- Set git to use your GitHub `noreply` email (see setup guide)
- Keep **push protection** on (Settings → Code security) so GitHub blocks known secret formats
- Use `gh auth login` or Git Credential Manager: never paste a token into a file or a chat
- Do not store portfolio repos inside a company-synced folder (e.g. corporate OneDrive), and don't copy work files into them

## If something leaks
1. **Credential?** Revoke/rotate it immediately. Assume it's compromised the moment it was pushed.
2. Make the repo private temporarily.
3. Remove it from history (`git filter-repo` or BFG), then force-push.
4. Tell your employer's IT/security team if it was company data or credentials.
5. Contact GitHub Support to purge cached views if needed.
