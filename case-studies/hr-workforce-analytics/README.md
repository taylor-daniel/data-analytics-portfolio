# HR & Workforce Analytics Suite: From Manual HR Reports to Automated Workforce and Employee Experience Dashboards

> **Summary:** Replaced a multi-day manual HR reporting cycle with an automated pipeline and a Power BI dashboard suite covering headcount, attrition, workforce composition and employee experience, refreshed weekly and reconciled against the HR system.

`Databricks` `PySpark` `Delta tables` `Microsoft Fabric` `Power BI` `DAX` · **Domain:** Workforce / people analytics · **Role:** People Data Analyst · **Period:** Feb 2023 – Jun 2026

---

## 1. Overview
An integrated view of employee experience, talent management and workforce dynamics across the group. The dashboards show how many people the organisation employs and how that workforce is distributed by level, cadre, gender and generation, alongside how hiring and exits evolve over time, so leadership can see where the organisation is expanding and how its composition is shifting year to year.

Attrition is a major theme: exits by cadre, year and generation, new hires versus exits, whether headcount growth is outpacing attrition, and where turnover concentrates by legal entity and business area.

Employee experience is the other core focus. Exit interview data surfaces why people leave, while survey-based indices capture overall experience, recommendation propensity (eNPS), and perceptions of performance management, pay, line manager relationship, and reasons for joining. Together these connect people outcomes — hiring, retention, demographics — with the quality of the employee experience, so HR and leadership can target interventions where they will matter most.

## 2. Business Problem
HR reporting was produced manually: data pulled separately from multiple HR systems, cleaned by hand in spreadsheets, and presented in static slide decks. Compiling, validating and distributing basic headcount and attrition updates took several days each month, which left little time for actual analysis.

As a result, leadership could not easily see consistent, up-to-date workforce trends by entity, cadre, generation or reason for exit, and there was no single reliable source connecting headcount growth, attrition hotspots and employee experience in one place.

## 3. Objective
- Eliminate the repeated manual spreadsheet analysis behind each reporting cycle
- Give management and leadership a workforce overview at a glance, with enough depth to draw their own insights
- Provide one consistent, reconciled source for workforce KPIs across the group

## 4. Scope

| Area | In the suite |
|---|---|
| Workforce / headcount | ✅ |
| Attrition | ✅ |
| Employee experience | ✅ |
| Performance management | ✅ |
| Talent management | ✅ |
| Strategic HR KPIs | ✅ |
| Workforce planning | ✅ |
| Learning & development | Data modelled and loaded; dashboard pending |

## 5. Data

| Source (anonymised) | Content | Role in the analysis |
|---|---|---|
| HR information system export | Employee master and movement records | Headcount, composition, joiners and leavers |
| Learning & development records | Training and development activity | L&D reporting (in progress) |
| Exit interview responses | Stated reasons for leaving | Attrition drivers |
| Pulse and experience surveys | Experience, eNPS and perception measures | Employee experience indices |

**Refresh:** weekly.

**Handling personal data:** the suite reports aggregated workforce measures. No individual records, salaries or identifiable results are published in this case study, and no figures are shown at a level that could identify a person or a small team.

## 6. Tools & Technologies
- **Azure Data Lake Storage** — landing zone for source extracts
- **Microsoft Fabric** — central engineering layer and the serving layer for reporting
- **Databricks** — execution environment for the transformation notebooks
- **PySpark** — profiling, cleaning, standardisation, aggregation and data-quality checks
- **Delta tables** — storage format for transformed outputs
- **Power BI + DAX** — data model, measures and dashboards, on a scheduled refresh

**Flow:** Source systems → ADLS → engineering layer in Microsoft Fabric → Databricks notebooks → files and tables in Fabric → Power BI.

## 7. Approach

1. **Ingestion** — Source data landed in ADLS, then into the engineering layer in Microsoft Fabric, which the Databricks notebooks connected to for transformation.
2. **Profiling** — Checked dataset structure, data types, missing values, duplicates and overall quality before cleaning, to understand the condition of the data.
3. **Cleaning & standardisation** — Trimmed and standardised text fields so that keys and categories matched across datasets.
4. **Aggregation** — Built the reporting measures: headcount by year, total and average headcount, attrition and attrition trend, employee experience index trend, active and exited employees by gender and generation, leadership distribution, and new hires year on year.
5. **Data-quality checks** — Null, duplicate, unmatched-key and row-count checks, with results displayed at every transformation stage rather than only at the end.
6. **Data modelling** — Modelled the output in Power BI as a star schema: an employee fact table related to the promotion, learning and development, exit and survey tables, so every page filters consistently from one model.
7. **Measure development** — DAX measures for attrition rate, average tenure, headcount trend, employee experience index, employee satisfaction and eNPS.
8. **Dashboard development** — Pages for workforce overview and composition, attrition and hotspots, and employee experience.
9. **Validation** — Reconciled headcount and exits against the HR information system.
10. **Delivery & adoption** — Outputs written to files and tables in Microsoft Fabric, which Power BI connects to on a scheduled weekly refresh.

## 8. Key Analysis
- Headcount growth and new hires over time
- Workforce composition by cadre, leadership level, gender and generation
- Attrition levels and trends over time
- New hires versus exits, and whether growth outpaces attrition
- Attrition hotspots by department, business area and legal entity
- Employee experience and engagement indices
- Key reasons for joining and for leaving
- Perceptions of performance management, pay and line manager relationship

## 9. Key Insights
- Headcount is rising steadily, with growth consistently outpacing attrition, while exits have declined over recent years.
- Attrition is not evenly spread: it concentrates in a small number of departments with markedly high turnover, and in junior cadres and younger generations, while most other areas stay relatively stable.
- The workforce remains predominantly millennial but is shifting gradually toward more Gen Z representation and a more balanced gender mix, with most employees still at non-management levels.
- Employee experience is strong overall — consistently high experience and recommendation scores, and positive views of line managers and performance evaluation. Exits are driven largely by career advancement and relocation rather than dissatisfaction with pay or working relationships.

*(Findings are stated in direction and pattern only; no figures that could identify the organisation or any individual are published.)*

## 10. Validation & Quality Assurance
- Headcount and exits reconciled against the HR information system
- Data-quality check results displayed at each transformation stage, so a discrepancy can be traced to the step that caused it
- KPI definitions agreed with HR before the measures were built, so the dashboard and HR's own records mean the same thing

## 11. Business Impact

**Manual work reduced** — A reporting cycle that took several days each month to compile, validate and distribute became a dashboard on a weekly automated refresh. The manual pulling, hand-cleaning and deck-building steps were removed.

**Visibility gained**

- Consistent, current workforce trends by entity, cadre, generation and reason for exit, in one place
- Whether headcount growth is outpacing attrition, year by year
- Where attrition concentrates, rather than a single group-level rate
- How composition is shifting across gender, generation and leadership level
- Employee experience and eNPS trends alongside the headcount and attrition picture

**Decisions enabled** — Leadership and HR can target retention effort at the specific departments, cadres and generations where turnover concentrates, rather than treating attrition as a single group-wide number, and can connect those decisions to what exit interviews and surveys say about why people leave.

**Measures delivered** — Total and average headcount, headcount by year, attrition rate and trend, new hires year on year, active and exited employees by gender and generation, leadership distribution, employee experience index, employee satisfaction, and eNPS.

## 12. My Contribution

| I did | Others did |
|---|---|
| Built the ingestion and transformation pipeline in Databricks with PySpark | HR defined the KPIs and the definitions behind them |
| Profiled, cleaned and standardised the HR, L&D, exit and survey datasets | A data/IT team provided access to the source systems and platform |
| Implemented the data-quality checks at every stage | |
| Built the Power BI data model: employee fact table related to promotion, L&D, exit and survey tables | |
| Wrote the DAX measures and built the dashboard pages | |
| Reconciled headcount and exits against the HR system | |

## 13. Challenges & Solutions

| Challenge | Type | Solution |
|---|---|---|
| Data pulled from several HR systems, cleaned by hand, with no single source | Business / Technical | Built one pipeline that lands, cleans and standardises every source into reconciled tables |
| Inconsistent text values and categories across datasets | Technical | Trimmed and standardised fields so keys and categories matched before modelling |
| Reporting areas (promotion, L&D, exits, surveys) sitting in separate datasets | Technical | Modelled them in Power BI around a single employee fact table, so every page filters consistently |
| Numbers had to be trusted by HR before anyone would use the dashboard | Business | Agreed KPI definitions with HR up front and reconciled headcount against the HR system |
| Group-level attrition rates hid where the problem actually was | Analytical | Broke attrition down by cadre, generation, department and legal entity to expose hotspots |

## 14. Lessons Learned
- **Technical:** standardise keys and categories before modelling; build data-quality checks into the pipeline rather than after it; a single fact table with clean relationships is what keeps every dashboard page consistent.
- **Business:** agreeing what a KPI means is harder, and more valuable, than building the measure. People data also needs care that other domains don't: aggregate far enough that no individual is identifiable, and reconcile to the system HR already trusts, or the dashboard won't be used.

## 15. Future Improvements
- Complete the learning & development dashboard on the data already modelled
- Attrition forecasting rather than trend reporting alone
- Alerting when a KPI crosses a threshold, instead of manual inspection
- Point-in-time snapshots to support historical "as at" reporting

## 16. Artefacts
No screenshots or code from the production solution are published. Planned: dashboard views rebuilt on **synthetic** employee data, a data model diagram with generic table names, and sample DAX measures (attrition rate, average tenure, headcount trend, employee experience index, eNPS).

---

**Topics:** `hr-analytics` `people-analytics` `workforce-analytics` `attrition-analysis` `power-bi` `dax` `data-modeling` `pyspark` `databricks` `microsoft-fabric` `business-intelligence` `kpi-dashboard`

<sub>Anonymised case study. No employee, salary, performance or organisational data is published, and no figures are shown at a level that could identify an individual or a team.</sub>
