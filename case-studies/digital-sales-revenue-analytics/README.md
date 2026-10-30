# Digital Sales & Revenue Analytics: Building a Trusted View of Digital Channel Performance

> **Latest addition (October 2026):** extended the reporting with an agent dimension — an agent reference table joined to the web revenue table on the agent code, giving agent-level attribution, an agent leaderboard and agent-by-product analysis.

> **Summary:** Built a PySpark transformation and data-quality layer on Databricks that turned raw quote, policy, product and transaction data into a reliable view of product traction, policy sales and premium generated through digital platforms, validated against the transaction system and delivered as a Power BI report.

`Databricks` `PySpark` `Delta / Parquet` `Microsoft Fabric` `Power BI` · **Domain:** Digital transformation · Revenue analytics · **Industry:** Insurance · **Role:** BI & Analytics Engineer · **Period:** 2026 · **Scope:** 3 product categories across 2 digital channels

---

## 1. Overview
An insurance business selling through digital platforms needed to understand how those channels were performing: which products were gaining traction, how many quotes converted into policies, and how much premium the digital channels generated. Nothing existed yet: the source connection, the transformation and the reporting all had to be built from scratch, and the data lived in separate systems rather than in one table. I built the transformation and data-quality logic in Databricks using PySpark, validated the outputs against the transaction system, and delivered the reporting layer in Power BI.

## 2. Business Problem
Management had limited visibility into the performance of digital platforms:

- Product traction on digital channels was not easy to see
- Policy sales and premium attributable to digital platforms were not readily measurable
- There was no existing pipeline or report to build on; the data sources had to be identified and connected first
- Required data sat in separate tables (quote, policy, product and transaction), so nothing could be answered without joining them reliably

## 3. Objective
- Improve visibility into **product traction**, **policy sales** and **premium revenue** generated through digital platforms
- Produce clean, consistent, validated datasets that reporting could rely on
- Provide a basis for assessing **return on investment** in the digital platforms

## 4. Data

| Source (anonymised) | Content | Role in the analysis |
|---|---|---|
| Digital quote data | Quote records raised on the digital platforms | Demand and conversion |
| Policy data | Policy information | Policy counts, product and channel attribution |
| Product reference data | Product and product-category information | Grouping and classification |
| Transaction data | Premium and transactions | Revenue, and the benchmark for validation |
| Agent reference data | Agent and platform-user records: identifying code and descriptive attributes | Agent-level attribution and slicing (added October 2026) |

**Data challenges**

- Inconsistent formatting (leading and trailing spaces, non-standard values) that broke joins and grouping
- Duplicate records and duplicated columns across the joined datasets
- Identifying a dependable primary key across systems
- Mismatched product codes, caused by closely related codes referring to the same product
- Date handling: transaction date and issue date did not align, so the correct date had to be chosen per measure
- Duplicate agent records in the agent reference data, which would have fanned out the revenue rows on join and inflated every agent total

## 5. Tools & Technologies

- **Azure Data Lake Storage** — landing zone for source data
- **Microsoft Fabric** — central engineering layer, and the serving layer for reporting
- **Databricks** — development and execution environment for the transformation notebooks
- **PySpark** — cleaning, standardisation, joins, filtering, classification, aggregation and data-quality checks
- **Delta and Parquet tables** — storage format for transformed outputs
- **Power BI** — report and dashboard layer, on a scheduled refresh

**Flow:** Source → ADLS → engineering layer in Microsoft Fabric → Databricks notebooks (transformation) → files and tables in Fabric → Power BI.

## 6. Approach

1. **Ingestion** — Source data landed in ADLS, then into the engineering layer in Microsoft Fabric, which the Databricks notebooks connected to for transformation.
2. **Profiling** — Checked dataset structure, data types, missing values, duplicates and overall quality to understand the condition of the data before cleaning.
3. **Cleaning & standardisation** — Trimmed and standardised text fields so keys and categories matched across datasets.
4. **Integration** — Joined the quote, policy, product and transaction datasets on validated keys.
5. **Filtering** — Removed duplicated columns and draft policies so only real business records were counted.
6. **Classification** — Derived source, channel, product group, product type and quote status, using the policy number structure.
7. **Agent dimension (added October 2026)** — Imported the agent reference table, de-duplicated it to one row per agent code, and joined it to the web revenue table on the agent code carried on the revenue records. The de-duplication came first: joining a dimension that is not unique on its key multiplies the fact rows and quietly inflates every total.
8. **Aggregation** — Built weekly, monthly and yearly summaries: policy counts, revenue, revenue by product category, revenue by month, and channel and source by product revenue.
9. **Data-quality checks** — Null checks, duplicate checks, unmatched-key checks and row counts, with results displayed at every transformation stage rather than only at the end.
10. **Validation** — Compared transformed outputs against the transaction system.
11. **Delivery & adoption** — Wrote outputs to files and tables in Microsoft Fabric, which Power BI connects to on a scheduled refresh.

## 7. Key Analysis
- Product traction across digital platforms
- Policy sales generated through digital channels
- Premium revenue by channel, source and product, covering three product categories (motor, travel and household lines) across two digital channels
- Quote-to-policy conversion
- Trends over time by year and month
- Platform comparison by revenue
- Agent-level attribution: revenue and policies by agent, ranked (added October 2026)
- Agent by product and channel mix, and agent revenue trend over time

## 8. Key Insights
The reporting compares how the digital distribution channels (for example a public web journey versus an intermediary portal) contribute to revenue and policy volume, both overall and product by product. It shows which product categories and which individual products drive performance, how that shifts month to month and year on year, and how the portfolio splits between the major categories (motor, travel and household lines) and the long tail of smaller products.

## 9. Business Impact

**Visibility gained**

- Channel performance: how each digital channel contributes to revenue, overall and per product
- Product-level performance: the largest and smallest revenue contributors in the portfolio
- Portfolio mix: how revenue is distributed across the major product categories and everything else
- Efficiency and demand quality: overall quote-to-policy conversion alongside policy volumes
- Value per record: average revenue per policy overall, and by product category
- Seasonality: monthly revenue movement, and which periods are peak and trough
- Year-on-year direction across the time series
- Data recency: when the report last refreshed, so stakeholders know how current the figures are
- Agent-level performance: which agents generate the revenue, what they sell and how that moves over time, with filters and drill-through so users answer their own agent questions

**Decisions enabled** — The reporting was designed to support decisions on which distribution channels and product categories to prioritise and optimise, in order to grow digital revenue and policy volume over time. The agent dimension extends that from channel level down to the individual agent, supporting decisions on where to focus agent engagement and support.

**Measures delivered** — Total revenue across all products, revenue by product category, average revenue by product category, quote-to-policy conversion, and policy counts, across three product categories and two digital channels.

## 10. My Contribution

| I did | Others did |
|---|---|
| Identified and connected the required source tables | A data/IT team provided access to the source systems and platform |
| Built the PySpark transformations in Databricks: cleaning, joins, filtering, classification and aggregation | Business stakeholders defined the requirements |
| Implemented the data-quality checks at every stage | Business stakeholders confirmed row counts and premium totals during validation |
| Validated outputs against the transaction system | |
| Built the Power BI report on the transformed tables | |

## 11. Challenges & Solutions

| Challenge | Type | Solution |
|---|---|---|
| No existing pipeline or report; required data spread across separate systems | Technical / Business | Traced the data back to the quote, policy, product and transaction tables and designed the joins to bring them together |
| Inconsistent text values breaking joins and groupings | Technical | Trimmed and standardised fields before joining |
| Identifying a dependable primary key across datasets | Technical | Profiled candidate keys and tested join results before accepting them |
| Closely related product codes referring to the same product | Technical / Business | Classified records into product groups rather than relying on raw codes |
| Transaction date and issue date not aligning | Technical | Chose the appropriate date per measure and applied it consistently |
| Trusting that transformed numbers were correct | Technical / Business | Reconciled outputs against the transaction system with stakeholders |
| Duplicate rows in the agent reference table | Technical | De-duplicated to one row per agent code before joining, then re-checked revenue totals against the pre-join figures to confirm nothing had fanned out |

## 12. Validation & Quality Assurance
- Total premium reconciled by source against the transaction system
- Row counts and total premium per product confirmed with the business stakeholders who own those figures
- Data-quality check results displayed at each transformation stage, so a break could be traced to the step that caused it

## 13. Lessons Learned
- **Technical:** standardise keys before any join; build data-quality checks into the pipeline rather than bolting them on afterwards; display results at each stage so problems surface early.
- **Business:** understand the business logic before transforming, or the work turns into back-and-forth rework. Reconciliation against a system the business already trusts is what drives adoption.

## 14. Future Improvements
- Automated scheduling across the full pipeline
- Alerting on data-quality check failures rather than manual inspection
- A gold layer in a medallion architecture for the serving tables
- A full quote-to-policy conversion funnel, rather than a single conversion rate

## 15. Artefacts
No code or screenshots from the production solution are published. Illustrative versions of the reporting — revenue by product category and channel, and an indexed monthly trend — are rebuilt on **synthetic** data on the [portfolio site](https://taylor-daniel.github.io/#case-digital). A sanitised, runnable version of the standardise → join → classify → aggregate → quality-check pattern is published separately as [pyspark-data-quality-pipeline](https://github.com/taylor-daniel/pyspark-data-quality-pipeline), built on synthetic data with tests. Still planned: an architecture diagram with generic system names.

---

**Topics:** `pyspark` `databricks` `data-engineering` `etl` `data-quality` `data-validation` `revenue-analytics` `digital-transformation` `insurance-analytics` `analytics-engineering` `microsoft-fabric` `power-bi`

<sub>Anonymised case study. The company, its platforms, product names and all identifying figures have been removed or generalised; no customer, policy or financial records are published.</sub>
