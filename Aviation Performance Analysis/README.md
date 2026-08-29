# ✈️ Aviation Operations & Flight Performance Analytics

An end-to-end Azure data engineering project that ingests monthly BTS (Bureau of Transportation Statistics) flight on-time performance data, transforms it through a medallion architecture, and serves it through a 5-page Power BI report.

*Portfolio project — demonstrates production-oriented data engineering patterns (idempotent loading, incremental processing, dimensional modeling) against a realistic dataset.*

---

## Architecture

```
BTS Source Files (.csv, monthly)
        │
        ▼
ADLS Gen2 (Bronze)  — flat structure: bronze/2026/2026_01.csv
        │
        ▼
Azure Data Factory  →  dynamic, metadata-driven pipeline (ForEach over new files)
        │
        ▼
Azure SQL Database  →  Control table (ingestion tracking) + Staging table
        │
        ▼
Azure Databricks (Silver)  →  PySpark cleansing + SCD Type 1 via Delta MERGE
        │
        ▼
Azure Databricks (Gold)  →  Star schema (dimensions + fact table), Unity Catalog
        │
        ▼
Power BI  →  5-page analytical report (via Databricks SQL Warehouse)
```

---

## Tech Stack

Azure Data Lake Storage Gen2 · Azure Data Factory · Azure SQL Database · Azure Databricks (PySpark) · Delta Lake · Unity Catalog · Power BI (DAX)

---

## 1. Storage Account (ADLS Gen2)

- **Account**: Data Lake Storage Gen2 enabled (hierarchical namespace: **Enabled**)
- **Container**: `bronze`
- **Structure**: `bronze/<year>/<year>_<month>.csv` — e.g. `bronze/2026/2026_01.csv`
- Flat, intentionally simple structure — no deep nesting

---

## 2. Azure SQL Database

**Schemas:** `Control`, `Staging`

| Object | Purpose |
|---|---|
| `Control.IngestionControl` | Tracks file-level ingestion status (`NEW`/`PROCESSING`/`SUCCESS`/`FAILED`/`RETRY`), row counts, timestamps, errors |
| `Staging.FlightData` | Raw, append-only landing table — never updated in place |
| `Control.usp_CheckFileStatus` | Determines whether a file is NEW / CHANGED / RETRY / ALREADY_PROCESSED |
| `Control.usp_UpdateIngestionStatus` | Updates status, row counts, timestamps, error messages |

Full DDL and stored procedures: [`sql/`](sql/)

---

## 3. Azure Data Factory

**Pipeline:** `PL_Initial_Load_FlightData`

**Parameters:**
| Name | Default | Purpose |
|---|---|---|
| `FolderPath` | `2026` | Year-folder to scan in Bronze |
| `SourceSystem` | `BTS` | Static feed label for Control table lookups |
| `DatasetName` | `FlightData` | Static dataset label for Control table lookups |

**Flow:**
```
GetMeta_FolderList → FE_ProcessFiles (ForEach, sequential)
   ├─ GetMeta_BronzeFile
   ├─ LKP_CheckFileStatus  (Control.usp_CheckFileStatus)
   └─ IF_ShouldProcess (NEW/CHANGED/RETRY only)
        ├─ SP_MarkProcessing → COPY_BronzeToStaging → SP_MarkSuccess
        └─ (on failure) → SP_MarkFailed
→ DatabrickAviationJob  (triggers Databricks Job: Silver → Gold)
```

**Trigger:** `TR_NewFileInBronze` — Storage Event, fires on Blob Created in `bronze/*.csv`

Trigger parameter mapping:
| Parameter | Value |
|---|---|
| `FolderPath` | `@last(split(triggerBody().folderPath, '/'))` |
| `SourceSystem` | `BTS` (static) |
| `DatasetName` | `FlightData` (static) |

Full pipeline JSON: [`adf/PL_Initial_Load_FlightData.json`](adf/PL_Initial_Load_FlightData.json)

---

## 4. Azure Databricks

**Catalog:** `aviation_ws` (Unity Catalog) → schemas `silver`, `gold`

**Notebooks:**
| Notebook | Purpose |
|---|---|
| `01_Silver_Transformation` | JDBC read from Staging → cleansing → natural key + change-detection hash → Delta MERGE (SCD Type 1) → `aviation_ws.silver.flight_data` |
| `02_Gold_Dimensional_Model` | Builds `DimAirline`, `DimAirport`, `DimDate` (append-only, resumable surrogate keys) and `FactFlight` (Delta MERGE) → `aviation_ws.gold.*` |

**Job:** both notebooks run as sequential tasks in one Databricks Job on **Serverless** compute, triggered by ADF's Databricks Job activity (not the Notebook activity, since this workspace is serverless-only).

Full notebook source: [`databricks/`](databricks/)

---

## 5. Power BI

**Connection:** Import mode, via Databricks SQL Warehouse (Server Hostname + HTTP Path from the SQL Warehouse's Connection Details tab)

**Model:** Star schema — `DimAirline`, `DimAirport`, `DimDate` → `FactFlight`, including a role-playing `DimAirport` relationship (Origin active, Destination via `USERELATIONSHIP`)

**Report pages:**
1. Executive Overview
2. Airline Performance
3. Airport & Route Performance
4. Delay Root Cause
5. Cancellation & Disruption

Report file: [`powerbi/Aviation_Report.pbix`](powerbi/Aviation_Report.pbix)

---

## Key Design Decisions

- **Dynamic ADF pipeline** — one pipeline handles every monthly file via `ForEach`; no reconfiguration needed as new months arrive
- **Idempotent ingestion control** — Control table + stored procedures ensure re-running never creates duplicates
- **SCD Type 1 via Delta MERGE** — composite natural key + change-detection hash decide update vs. insert vs. skip
- **Resumable surrogate keys** — dimension loads always continue from `max(key) + 1`, never reset, across monthly loads
- **Threshold-based ranking in Power BI** — route/airport rankings exclude low-volume outliers to avoid misleading small-sample results

---

## Repository Structure

```
├── adf/         → exported ADF pipeline JSON
├── sql/         → table DDL + stored procedures
├── databricks/  → Silver & Gold PySpark notebooks
├── powerbi/     → .pbix report file
├── docs/        → project walkthrough PDF + screenshots
└── README.md
```

---

## Data Source

[U.S. Bureau of Transportation Statistics — On-Time Performance Data](https://www.transtats.bts.gov/)

---

## Author

Built by Ajitkumar Sabat · [https://www.linkedin.com/in/ajitkumar-sabat-9a1720218/](#)
