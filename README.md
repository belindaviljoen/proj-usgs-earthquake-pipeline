# USGS Earthquake Data Pipeline - Assignement

This project simulates a real-world data engineering workflow — from ingestion to transformation and analysis — using a public dataset from the USGS Earthquake API. Everything is done locally using Python, with a proposed AWS architecture for automation and scalability.


## Project Overview

Over the past few days, I worked on a small pipeline to fetch and analyze global earthquake data from the [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/). The goal was to simulate a real-world scenario where raw JSON data is ingested, transformed into a structured format, and used for basic analysis — all using Python.

The pipeline is divided into three stages:
- **Data Ingestion** - Retrieving the past year’s earthquake events.
- **Transformation** - Converting JSON into a clean tabular format.
- **Analysis** – Calculating the average daily magnitudes, identifying the top 10 earthquakes, and estimating regional activity.

Each stage is modular and can be run independently.

> While building this, I ran into a few interesting challenges. For example, the `place` field in the USGS data doesn't follow a consistent format (some entries include both city and country, others only regions). To extract countries or regions, I used a basic string-splitting approach. It works for most cases, but I'd consider geolocation enrichment for more accuracy in a production setting.

The output is saved as `.csv` files, which makes it easy to review the results or plug into downstream tools. In a production environment, I'd likely make use of `.parquet` format due to its efficiency and support for schema evolution.


## Pipeline Structure

### 1. Data Ingestion

Fetch data for the past 365 days using the USGS API.

**Script**: `scripts/fetch_earthquake_data.py` 
**Output**: `data/usgs_earthquakes_raw.json`

### 2. Data Transformation

Extract and clean the following fields:
- Timestamp (converted to UTC datetime)
- Place
- Magnitude
- Longitude, Latitude, Depth
- Event Type

**Script**: `scripts/transform_earthquake_data.py` 
**Output**: `data/processed/earthquakes_transformed.csv`

### 3. Data Analysis

Performs:
- Average magnitude per day
- Top 10 largest earthquakes
- Count of earthquakes per country/region (based on place string)

**Script**: `scripts/analyze_earthquake_data.py` 
**Outputs**:
- `data/results/average_magnitude_per_day.csv`
- `data/results/top_10_largest_earthquakes.csv`
- `data/results/earthquakes_per_region.csv`

---

## Part 2: AWS Architecture Proposal

To scale and automate this pipeline, I designed an AWS-based architecture using the following services:

### Architecture Components

- **Amazon S3** – Store raw and processed files in separate prefixes (`/raw/`, `/processed/`)
- **AWS Lambda** – To handle scheduled ingestion and light processing.
- **AWS Glue** – Perform transformations and catalog data.
- **AWS Glue Data Catalog** – Store metadata for querying with Athena.
- **Amazon Athena** – Allow querying on processed data without setting up a database.
- **Amazon QuickSight** – For visualization and reporting.
- **CloudWatch Events** – Trigger Lambda functions on a schedule.


## Setup Instructions

### 1. Clone the Repo

Using bash:

git clone https://github.com/belindaviljoen/proj-usgs-earthquake-pipeline.git
cd proj-usgs-earthquake-pipeline

#### 2. Install Dependencies

pip install -r requirements.txt

#### 3. Run the pipeline

Using bash: 

**Step 1: Ingest the data from the USGS API**
python scripts/fetch_earthquake_data.py

**Step 2: Transform the raw JSON to tabular format**
python scripts/transform_earthquake_data.py

**Step 3: Perform analysis and export the results**
python scripts/analyze_earthquake_data.py