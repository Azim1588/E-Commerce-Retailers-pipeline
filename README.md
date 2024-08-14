# E-Commerce Retailers Pipeline Data Engineering Project

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

## Setup and Installation

### Prerequisites

- Python 3.8+
- Google Cloud SDK
- BigQuery API enabled
- Google Cloud Storage Bucket
- Service Account with necessary permissions

### Installation

#### Step 1: Set Up a Google Cloud VM

1. **Create a New VM Instance:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to **Compute Engine > VM instances**.
   - Click on **Create Instance**.
   - Configure the instance:
     - Choose a name for your instance.
     - Select a region and zone.
     - Choose the machine type (e.g., `e2-medium` for moderate usage).
     - Under **Boot disk**, select **Ubuntu 20.04 LTS**.
     - Click on **Create**.

2. **Connect to the VM Instance:**
   - Once the instance is running, click **SSH** to open a terminal window connected to your VM.

#### Step 2: Update and Install Dependencies

```bash
# Update the package list
sudo apt-get update

# Upgrade the existing packages
sudo apt-get upgrade -y

# Install Python 3.8 (if not already installed)
sudo apt-get install python3.8 python3.8-venv python3.8-dev -y

# Install pip
sudo apt-get install python3-pip -y

# Install Git (if not already installed)
sudo apt-get install git -y
                       
