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

## Setup and Installation
Prerequisites
Python 3.8+
Google Cloud SDK
BigQuery API enabled
Google Cloud Storage Bucket
Service Account with necessary permissions

## Installation
  ## Step 1: Set Up a Google Cloud VM
Create a New VM Instance:

Go to the Google Cloud Console.
Navigate to Compute Engine > VM instances.
Click on Create Instance.
Configure the instance:
Choose a name for your instance.
Select a region and zone.
Choose the machine type (e.g., e2-medium for moderate usage).
Under Boot disk, select Ubuntu 20.04 LTS.
Click on Create.
## 2: Connect to the VM Instance:

Once the instance is running, click SSH to open a terminal window connected to your VM.

## Step 2: Update and Install Dependencies

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

## Step 3: Install Mage AI
# Clone the Mage AI repository (or install via pip)
git clone https://github.com/mage-ai/mage-ai.git

# Change to the Mage AI directory
cd mage-ai

# Install Mage AI using pip
pip3 install .

# Alternatively, you can install it directly using pip:
pip3 install mage-ai

## Step 4: Set Up the Environment
# Create a new project directory
mkdir my_mage_project
cd my_mage_project

# Initialize a new Mage project
mage init my_project

## Step 5: Run Mage AI
Step 5: Run Mage AI

## Step 6: Access Mage AI Interface
Once the server is running, you can access the Mage AI interface by visiting the external IP of your VM in your browser at http://<YOUR_VM_EXTERNAL_IP>:6789.
Optional: Set Up a Firewall Rule for Port 6789
Allow Traffic on Port 6789:
Go to VPC Network > Firewall in the Google Cloud Console.
Click on Create Firewall Rule.
Name it mage-ai.
Set Targets to All instances in the network.
Set Source IP ranges to 0.0.0.0/0.
Set Protocols and ports to tcp:6789.
Click Create.
Now you can access the Mage AI interface through the browser using the VM's external IP.

## Step 7: Stop the Server
# To stop the Mage AI server, press Ctrl+C in the terminal where it is running.

                                 
