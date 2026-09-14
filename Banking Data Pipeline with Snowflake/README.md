# 🏦 Banking Data Pipeline with Snowflake

An enterprise-style **banking data pipeline** built using **Snowflake, SQL, and Python** to demonstrate batch ingestion, automated incremental processing, data transformation, historical data tracking, and analytics-ready dimensional modeling.

---

## 📌 Project Overview

This project simulates a banking data platform where synthetic banking data is ingested into Snowflake and processed through a **Bronze → Silver → Gold** architecture.

The pipeline supports both **initial data loading** and **incremental data ingestion** using Snowpipe, Streams, Tasks, and MERGE operations.

---

## 🏗️ Architecture

```text
                Python
                  │
                  │ Generate CSV Batches
                  ▼
        Snowflake Internal Stage
                  │
                  │ Snowpipe
                  ▼
             Bronze Layer
                  │
                  │ Stream
                  ▼
             Silver Layer
                  │
             Task + MERGE
                  ▼
              Gold Layer
                  │
                  ▼
               Power BI
```

---

## 🔄 Pipeline Flow

### 1. Data Generation

Python is used to generate synthetic banking data and create CSV files representing incoming banking records.

### 2. Initial Load

Initial CSV files are loaded into Snowflake Bronze tables.

### 3. Incremental Ingestion

New CSV batches are uploaded to the Snowflake Internal Stage.

**Snowpipe** automatically loads newly arrived files into the Bronze layer.

### 4. Bronze → Silver

Snowflake **Streams** capture new and changed records from Bronze tables.

Scheduled **Tasks** process the stream data and load it into Silver tables.

### 5. Silver → Gold

The Silver layer is transformed into analytics-ready Gold tables using SQL and **MERGE** logic.

SCD Type 1 and Type 2 logic is implemented where required for maintaining current and historical records.

### 6. BI Consumption

The Gold layer is designed for analytical reporting and can be connected to **Power BI** for banking dashboards and KPI analysis.

---

## 🥉 Bronze Layer

The Bronze layer stores raw ingested banking data.

Key characteristics:

- Raw source data
- CSV-based ingestion
- Snowflake Internal Stage
- Snowpipe ingestion
- Minimal transformation

---

## 🥈 Silver Layer

The Silver layer contains cleaned and transformed data.

Key processing includes:

- Incremental data processing
- Data cleansing
- Deduplication
- Stream-based change detection
- Task-based automation
- MERGE operations

---

## 🥇 Gold Layer

The Gold layer contains business-ready dimensional data designed for analytics.

The model includes banking entities such as:

- Customer
- Account
- Branch
- Transaction
- Date

The Gold layer follows **dimensional modeling principles** and is designed to support Power BI reporting.

---

## ⚙️ Snowflake Features Used

- Snowflake Architecture
- Internal Stage
- File Formats
- COPY INTO
- Snowpipe
- Streams
- Tasks
- MERGE
- SCD Type 1
- SCD Type 2
- RBAC
- Bronze / Silver / Gold Architecture
- Dimensional Modeling

---

## 🐍 Python Automation

Python is used to:

- Generate synthetic banking data
- Create incremental CSV batches
- Upload files to the Snowflake Internal Stage
- Simulate continuously arriving banking data

---

## 🔁 Incremental Processing

The project demonstrates an incremental data pipeline where new files are continuously introduced into the system.

```text
New CSV Batch
      ↓
Internal Stage
      ↓
Snowpipe
      ↓
Bronze
      ↓
Stream
      ↓
Task
      ↓
Silver
      ↓
MERGE / Transformation
      ↓
Gold
```

This approach avoids reprocessing the complete dataset for every incoming batch.

---

## 🧠 Key Concepts Demonstrated

- ETL / ELT
- Batch Data Ingestion
- Incremental Data Processing
- Snowpipe
- Change Data Capture using Streams
- Task-based Automation
- MERGE / Upsert Processing
- Data Deduplication
- SCD Type 1
- SCD Type 2
- Dimensional Modeling
- Star Schema
- Bronze / Silver / Gold Architecture
- Python Data Automation
- SQL Transformation

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Data Platform | Snowflake |
| Programming | Python |
| Query Language | SQL |
| Data Ingestion | Snowpipe, Internal Stage |
| Processing | Streams, Tasks, MERGE |
| Data Modeling | Dimensional Modeling, Star Schema |
| File Format | CSV |
| BI | Power BI |

---

## 📁 Project Structure

```text
Banking Data Pipeline with Snowflake/
│
├── Python Scripts/
│   ├── generate_initial_data.py
│   ├── incremental_batch01.py
│   ├── incremental_batch02.py
│   ├── upload_initial.py
│   └── upload_incremental.py
│
└── SQL/
    ├── 01_Setup.sql
    ├── Bronze.sql
    ├── Silver.sql
    ├── Gold.sql
    ├── Snowpipe.sql
    ├── Streams.sql
    ├── Task(bronze to silver).sql
    └── Task(silver to gold).sql
```

---

## 🎯 Project Objectives

- Build an end-to-end banking data pipeline using Snowflake.
- Demonstrate automated incremental data ingestion.
- Implement Bronze, Silver, and Gold data layers.
- Apply Streams, Tasks, Snowpipe, and MERGE operations.
- Implement SCD Type 1 and Type 2 transformations.
- Prepare analytics-ready data for Power BI reporting.

---

## 📊 Business Use Cases

The curated banking data can be used to analyze:

- Customer activity
- Account transactions
- Transaction volumes
- Branch-level performance
- Customer/account trends
- Historical customer and account changes
- Banking transaction KPIs

---

## 👨‍💻 Author

**Ajit Sabat**

Data Analyst | Power BI Developer | Azure | Snowflake | SQL | Python
