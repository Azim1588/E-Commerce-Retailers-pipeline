## Project Overview
This project focuses on building a data engineering pipeline for E-Commerce Retailers. The pipeline automates the process of extracting CSV files from Google Cloud Storage, transforming the data, and loading it into Google BigQuery. Finally, the data is visualized using Looker Studio to create insightful dashboards. The pipeline is orchestrated using Mage AI, which is hosted on a Google Cloud VM.

## Architecture

The pipeline architecture is designed to efficiently handle large volumes of data and consists of the following key components:

- **Data Ingestion**: CSV files are extracted from Google Cloud Storage.
- **Data Transformation**: Data transformations are performed using Mage AI, which runs on a Google Cloud VM.
- **Data Loading**: The transformed data is loaded into Google BigQuery.
- **Data Visualization**: The data in BigQuery is visualized using Looker Studio to create dashboards.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: The pipeline is developed in Python and requires version 3.8 or higher.
- **Google Cloud SDK**: Required for interacting with Google Cloud services.
- **Google BigQuery**: Used as the data warehouse for storing and querying transformed data.
- **Looker Studio**: Used for creating dashboards from the data in BigQuery.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/e-commerce-retailers-pipeline.git
cd e-commerce-retailers-pipeline
```

### 2. Set Up Google Cloud VM with Mage AI

#### a. Create a Google Cloud VM Instance

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to **Compute Engine** > **VM Instances**.
3. Click on **Create Instance**.
4. Choose the machine type and configuration as needed.
5. Set up the VM with a public IP address.
6. SSH into the VM once it's created.

## Step 3: Install Mage AI
# Clone the Mage AI repository (or install via pip)
git clone https://github.com/mage-ai/mage-ai.git

# Change to the Mage AI directory
cd mage-ai

# Install Mage AI using pip
pip3 install .

# Alternatively, you can install it directly using pip:
pip3 install mage-ai







   

