# AI Job Replacement Analysis using Hadoop Framework

## Project Overview

This project demonstrates a complete Big Data pipeline using the Hadoop ecosystem. The objective is to process and analyze an AI Job Replacement dataset using HDFS for storage, MapReduce for processing, and Hive for querying and analytics.

---

## Architecture

| Component   | Description |
|------------|------------|
| HDFS        | Distributed storage for large datasets |
| MapReduce   | Parallel data processing framework |
| Hive        | SQL-like querying on big data |
| Cloudera    | Hadoop execution environment |

---

## Data Flow

| Stage              | Description |
|-------------------|------------|
| Raw Data          | CSV dataset containing job-related information |
| HDFS              | Data stored in distributed format |
| MapReduce         | Data processing and aggregation |
| Hive              | Querying and analysis |
| Insights          | Final results and interpretations |

---

## Dataset Description

| Attribute                     | Description |
|-----------------------------|------------|
| job_role                    | Job title |
| industry                    | Industry category |
| automation_risk_percent     | Risk of automation |
| salary_before_usd           | Salary before AI impact |
| salary_after_usd            | Salary after AI impact |
| skill_demand_growth_percent | Growth in skill demand |
| remote_feasibility_score    | Remote work feasibility |

---

## HDFS Implementation

| Step | Command |
|------|--------|
| Create Directory | `hdfs dfs -mkdir /user/cloudera/kanchanproject` |
| Upload Dataset   | `hdfs dfs -put ~/Desktop/ai_job_replacement_2020_2026_v2.csv /user/cloudera/kanchanproject` |
| Verify Upload    | `hdfs dfs -ls /user/cloudera/kanchanproject` |

---

## MapReduce Implementation

### Task 1: Risk Classification

| Category   | Count |
|-----------|------|
| High Risk | 2368 |
| Low Risk  | 12632 |

### Task 2: Industry-wise Job Count

| Industry   | Count |
|-----------|------|
| IT        | XXXX |
| Finance   | XXXX |
| Healthcare| XXXX |

---

## Hive Implementation

### Database and Table Setup

| Step | Command |
|------|--------|
| Create Database | `CREATE DATABASE kanchan_db;` |
| Use Database    | `USE kanchan_db;` |

---

### Table Schema

| Column Name | Data Type |
|------------|----------|
| job_id | INT |
| job_role | STRING |
| industry | STRING |
| country | STRING |
| year | INT |
| automation_risk_percent | FLOAT |
| salary_change_percent | FLOAT |

---

### Load Data

| Command |
|--------|
| `LOAD DATA INPATH '/user/cloudera/kanchanproject/ai_job_replacement_2020_2026_v2.csv' INTO TABLE ai_jobs;` |

---

## Hive Queries and Results

### Risk Distribution

| Category | Count |
|----------|------|
| High Risk | 2368 |
| Low Risk  | 12632 |

---

### Industry-wise Analysis

| Industry | Job Count |
|----------|----------|
| IT       | XXXX |
| Finance  | XXXX |
| Healthcare | XXXX |

---

### Average Salary Change

| Metric | Value |
|--------|------|
| Average Salary Change | (Result from query) |

---

### Top Growing Job Roles

| Job Role | Growth Percentage |
|----------|------------------|
| Role 1   | Value |
| Role 2   | Value |

---

## Key Insights

| Insight No | Description |
|-----------|------------|
| 1 | Majority of jobs are low-risk, indicating stability |
| 2 | Some industries dominate job distribution |
| 3 | AI impacts salaries differently across skill levels |
| 4 | High-skill roles show strong growth |
| 5 | Remote work feasibility is increasing |

---

## Use of Generative AI

| Area        | Usage |
|------------|------|
| Code Generation | Mapper and Reducer scripts |
| Debugging       | Error fixing in Hadoop jobs |
| Query Writing   | Hive query generation |

---

## Conclusion

This project demonstrates how Hadoop can be used to process and analyze large datasets efficiently. By combining HDFS, MapReduce, and Hive, meaningful insights can be extracted from complex data.

---

## Author

| Name |
|------|
| Kanchan Kapri |
| Roll No : 1240258215  |
| Batch :  BCADS-23 |


## Happy Coding 
