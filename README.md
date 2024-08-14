## Project Overview
This project focuses on building a data engineering pipeline for E-Commerce Retailers. The pipeline automates the process of extracting CSV files from Google Cloud Storage, transforming the data, and loading it into Google BigQuery. Finally, the data is visualized using Looker Studio to create insightful dashboards. The pipeline is orchestrated using Mage AI, which is hosted on a Google Cloud VM.

## Architecture

The pipeline architecture is designed to efficiently handle large volumes of data and consists of the following key components:

- **Data Ingestion**: CSV files are extracted from Google Cloud Storage.
- **Data Transformation**: Data transformations are performed using Mage AI, which runs on a Google Cloud VM.
- **Data Loading**: The transformed data is loaded into Google BigQuery.
- **Data Visualization**: The data in BigQuery is visualized using Looker Studio to create dashboards.
![Project Architecture](image_url)
![Data Modeling](image_url)



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
Clone the Mage AI repository (or install via pip)
git clone https://github.com/mage-ai/mage-ai.git

 Change to the Mage AI directory
cd mage-ai

Install Mage AI using pip
pip3 install .

 Alternatively, you can install it directly using pip:
pip3 install mage-ai


## Step 4: Set Up the Environment
 Create a new project directory
mkdir my_mage_project
cd my_mage_project

 Initialize a new Mage project
mage init my_project

## Step 5: Run Mage AI
Start Mage AI server
mage start my_project

### Step 6: Access Mage AI Interface

Once the server is running, you can access the Mage AI interface by visiting the external IP of your VM in your browser at `http://<YOUR_VM_EXTERNAL_IP>:6789`.

#### Optional: Set Up a Firewall Rule for Port 6789

**Allow Traffic on Port 6789:**

1. Go to **VPC Network > Firewall** in the Google Cloud Console.
2. Click on **Create Firewall Rule**.
3. Name it `mage-ai`.
4. Set **Targets** to `All instances in the network`.
5. Set **Source IP ranges** to `0.0.0.0/0`.
6. Set **Protocols and ports** to `tcp:6789`.
7. Click **Create**.

Now you can access the Mage AI interface through the browser using the VM's external IP.

### Step 7: Stop the Server

To stop the Mage AI server, press `Ctrl+C` in the terminal where it is running.

### 3. Data Storage in BigQuery

The transformed data is then loaded into a BigQuery data warehouse. This step involves creating and populating fact and dimension tables that are optimized for reporting.

### 4. Dashboard & Reporting

Once the data is in BigQuery, it can be connected to Looker Studio (formerly Google Data Studio) to create interactive dashboards and reports. These dashboards provide insights into sales performance, customer behavior, and other key metrics.

### 5. Dashboard & Reporting

Once the data is in BigQuery, it can be connected to Looker Studio (formerly Google Data Studio) to create interactive dashboards and reports. These dashboards provide insights into sales performance, customer behavior, and other key metrics.

![Dashboard](image_url)










   

