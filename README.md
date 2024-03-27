<div>
  <img src="https://raw.githubusercontent.com/hsviscarra/RealEstateAnalysis/main/Static_files/retail_image.jpeg" style="width: 100%; height: 500px;">
</div>

## REAL STATE DATA ANALYSIS - CONNECTICUT STATE



## 1. Objective

The objective is to analyze the real estate price evolution of the propoerties sold in Connecticut from 2001 to 2021. The analysis will be perfomed by town and property type.


## 2. Problem statement

Knowing about the evolution of prices may help investors and individual home-owners to make better decisions. 
For investors to focus their effort on markets that are experiencing an increase in the prices to maximize their profits.
For home-owners which great part of their wealth is invested in their own homes, to buy in areas with value appreciation.

As an illustrative example, this project uses the Connecticut property sales dataset:

[Data source](https://catalog.data.gov/dataset/real-estate-sales-2001-2018)


## 3. Data architecture 

<img src="https://raw.githubusercontent.com/hsviscarra/RealEstateAnalysis/main/Static_files/Data%20Architecture.png">

The data was extracted using Mage. The extraction was performed using the url address to the data which is permanently updated. The pipeline consisted of the following steps:
1. Extract data from web page repository
2. Transform data types, column names, and filter out bad data such as sold prices with zero dollars.
3. Load the data in Google Cloud
4. Activate the process to run ever month. The updates performed by the State government are not done in specific periods. However, we ran the analysis in a monthly basis to check for any updats.
5. Run DBT in the cloud to build some models using SQL based on a samll star schema model with fact, dimension tables and aggregate tables.
6. Sink the data in BigQuery wharehouse
8. Using Google Cloud to build a small dashboard
<br>
<div>
<img src="https://raw.githubusercontent.com/hsviscarra/RealEstateAnalysis/main/Static_files/Dashboard%20example.png">
</div>
<br>
<br>

[Google Report] (https://lookerstudio.google.com/s/hqg23DQPT64)

## 4. Techonologies used
- Cloud: Google Cloud (GCP)
- Workflow orchestration: Mage
- Data Warehouse: BigQuery
- Batch processing: DBT
- Dashboard: Google Data Cloud



## 5. How to run the code.

### 5.1. Clone the repository
This repo contains the files of the project. In case of Mage (used for data orchestration) the repor contains a Docker Compose template for getting started with a new Mage project. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/). 

You can start by cloning the repo:

```bash
git clone https://github.com/hsviscarra/RealEstateAnalysis.git [name_of_the_folder]
``

Navigate to the repo:

```bash
cd [name_of_the_folder]
```

### 5.2 Build the container using Docker compose build (This command to build image based on the Docker compose and Docker file provided)

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, you can navigate to http://localhost:6789 in your browser to start building / modifying the pipelines

### 5.3 Changes in io_config.yml -> GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/[name_of_json_payload].json"

### 5.4 Open a google cloud free account to:
   - Create a storage / bucket to dump the data
   - Create a service account json payload with owner permissions to connect Mage to GCP

### 5.5 Create an account in DBT cloud and linked to you repo
Make the adjustements in the models

### 5.6 Open Goolge Data Cloud and connect it to your BigQuery account
Perform changes in the dashboard

## Assistance

1. [Mage Docs](https://docs.mage.ai/introduction/overview): Mage functionality or concepts.
2. [DBT Docs](https://docs.getdbt.com/docs/introduction): DBT documents 
4. [Google Data Studio](https://lookerstudio.google.com/navigation/reporting): Google Data Studio documents




