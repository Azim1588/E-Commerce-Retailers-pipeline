# E-Commerce Retailers Pipeline_Data Engineering_project

This repository contains the code and resources for building a data engineering pipeline for an E-Commerce Retailer. The pipeline is designed to extract data from CSV files stored in Google Cloud Storage, process and transform the data, and load it into BigQuery for analysis and reporting. Finally, the data is visualized using Looker Studio to create comprehensive dashboards.

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Setup and Installation](#setup-and-installation)
- [Data Pipeline Steps](#data-pipeline-steps)
  - [1. Data Ingestion](#1-data-ingestion)
  - [2. Data Processing & Transformation Layer](#2-data-processing--transformation-layer)
  - [3. Data Storage in BigQuery](#3-data-storage-in-bigquery)
  - [4. Dashboard & Reporting](#4-dashboard--reporting)
- [How to Run the Pipeline](#how-to-run-the-pipeline)
- [Contributing](#contributing)
- [License](#license)

## Architecture Overview

```plaintext
+---------------------+        +-----------------------+        +-------------------+        +---------------------+
|    Data Ingestion    |        |   Data Processing &   |        |    Data Storage   |        |   Dashboard / BI    |
|   (Batch Processing) |  --->  |  Transformation Layer |  --->  |      Layer        |  --->  |    Visualization    |
|   +---------------+  |        |   +----------------+  |        |   +------------+  |        |   +-------------+   |
|   |  CSV Files    |  |        |   | Data Cleaning  |  |        |   | Data Lake   |  |        |   |  Dashboard   |   |
|   | (Sales, Cust. |  |        |   |  & Filtering   |  |        |   |   (S3)      |  |        |   |  Platform    |   |
|   |  Info, etc.)  |  |        |   +----------------+  |        |   +------------+  |        |   |  (Power BI,  |   |
|   +---------------+  |        |   +----------------+  |        |   +------------+  |        |   |  Tableau,    |   |
+---------------------+        |   | Data Transform. |  |        |   | Data Warehouse|  |        |   |  Looker     |   |
                                 |   |  & Aggregation |  |        |   |   (BigQuery) |  |        |   |  Studio)    |   |
                                 |   +----------------+  |        |   +------------+  |        |   +-------------+   |
                                 |   +----------------+  |        |   +------------+  |        |                     |
                                 |   |  Data Joining  |  |        |   | Data Mart   |  |        |                     |
                                 |   |  & Merging     |  |        |   |   (Parquet) |  |        |                     |
                                 |   +----------------+  |        |   +------------+  |        |                     |
                                 +-----------------------+        +-------------------+        +---------------------+
