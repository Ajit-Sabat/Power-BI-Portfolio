# Azure Cost Analysis Dashboard

## Overview
The **Azure Cost Analysis Dashboard** is a Power BI report designed to provide comprehensive insights into Azure cloud expenditures across multiple years, regions, and services. It enables organizations to track retail costs, analyze spending trends, and identify cost optimization opportunities.

The dashboard consolidates data from Azure billing sources and presents it in an interactive and easy-to-navigate format, helping decision-makers understand where costs are concentrated and how they evolve over time.

---

## Objectives
- Monitor Azure costs across **regions, services, and years** (2016–2024).  
- Identify **high-cost services** and **regions** contributing most to expenses.  
- Analyze **year-over-year** and **month-over-month** spending trends.  
- Support **cost transparency**, **governance**, and **budget planning**.

---

## Key Insights
- The **top five services** account for **over 99%** of total retail costs.  
- **Storage** and **Compute** services represent the largest cost segments.  
- **Consumption-based costs** contribute approximately **66%** of the total.  
- Cost activity peaks in **March** and **October**, suggesting seasonal demand patterns.  
- **Europe** and **Americas** regions represent the highest retail costs.

---

## Tools and Technologies
- **Power BI Desktop** – Data modeling and visualization.  
- **Power Query** – Data transformation and cleansing.  
- **DAX (Data Analysis Expressions)** – KPI and measure creation.  
- **Azure Cost Data** – Source of transactional and billing data.

---

## Data Model and Preparation
The dataset was sourced from Azure billing records covering multiple services and regions. Data preparation steps included:
- Cleaning and standardizing fields such as service family, geography, and tags.  
- Aggregating cost and transaction data across years.  
- Establishing relationships for time-series analysis and hierarchical filtering.  
- Creating calculated measures for retail cost, transactions, and trends using DAX.

---

## Dashboard Structure

### 1. Home Page
Provides a high-level overview of key metrics and trends:
- Total Retail Cost: **$105.8M**  
- Total Transactions: **110,608**  
- Unique Regions: **66**  
- Unique Services: **169**  
- Unique Products: **1,108**  
- Share of **Reservation** vs **Consumption** costs.

**Visuals Include:**
- Retail cost breakdown by type.  
- Monthly cost and transaction trends.  
- Month-over-month (MoM) change analysis.  
- Retail cost distribution by geography.

---

### 2. Region Analysis Page
Breaks down cost and transaction data by:
- **Geography**, **Country**, **Location**, and **Tags**.  
- Highlights cost concentration across **Americas**, **Europe**, and **Government** regions.  
- Provides transparency into regional consumption patterns and spending behavior.

---

### 3. Services Analysis Page
Focuses on cost by service category and product name:
- Analyzes **Service Family**, **Service Name**, and **Product Name** dimensions.  
- Identifies top cost drivers such as **Storage Reserved Capacity** and **Azure NetApp Files**.  
- Enables comparison of service utilization and transaction volume over multiple years.

---

## Business Impact
The Azure Cost Analysis Dashboard supports:
- **Cloud cost optimization** by identifying high-expenditure areas.  
- **Budget allocation and forecasting** based on usage trends.  
- **Strategic decision-making** for resource reallocation.  
- Improved **financial accountability** and **cost transparency**.

---

## How to Use
1. Open the `.pbix` file in **Power BI Desktop**.  
2. Connect or refresh the data source (Azure billing dataset).  
3. Use the filters to explore data by **Year**, **Month**, **Geography**, or **Service Family**.  
4. Navigate between pages using the left-hand menu: **Home**, **Region**, and **Services**.

---

## Dashboard Preview

| Page | Description | Preview |
|-------|--------------|----------|
| **Home Overview** | Summary of KPIs, trends, and geographic cost breakdown. | ![Home Dashboard](https://github.com/Ajit-Sabat/Power-BI-Portfolio/blob/main/Azure%20Cost%20Analysis/Azure%20Home.png) |
| **Region Analysis** | Cost and transactions by geography and country. | ![Region Dashboard](<your-image-link-here>) |
| **Services Analysis** | Cost distribution by service and product. | ![Services Dashboard](<your-image-link-here>) |


---

## Learning and Technical Takeaways
- Designed a structured Power BI data model for multi-year Azure cost data.  
- Utilized DAX measures for trend analysis and key performance indicators.  
- Implemented dynamic filtering and navigation for enhanced interactivity.  
- Demonstrated the use of Power Query for data cleaning and automation.

---

## Conclusion
The **Azure Cost Analysis Dashboard** provides an end-to-end view of Azure cloud expenditure, empowering stakeholders to make informed financial and operational decisions. Through effective data modeling, visualization, and analysis, it delivers actionable insights that support cost optimization and long-term resource planning.
