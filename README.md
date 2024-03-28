<div>
  <img src="https://raw.githubusercontent.com/hsviscarra/RealEstateAnalysis/main/Static_files/retail_image.jpeg" style="width: 100%; height: 500px;">
</div>

## REAL STATE DATA ANALYSIS - CONNECTICUT STATE


## 1. Objective

The objective is to conduct a comprehensive analysis of the real estate price trends observed in Connecticut from 2001 to 2021. 
This analysis examines the evolution of property prices, categorizing data by both town, property and residential type to provide 
a thorough understanding of market dynamics. 


## 2. Problem statement

Understanding the evolution of prices is crucial for investors and individual homeowners alike, empowering them to make informed decisions. 
Investors can strategically allocate their resources to markets experiencing price increases, maximizing potential profits. 
Similarly, homeowners, whose significant portion of wealth is often invested in their properties, can benefit by purchasing in areas with appreciating values.

To illustrate this principle, this project utilizes the Connecticut property sales dataset:

[Data source](https://catalog.data.gov/dataset/real-estate-sales-2001-2018)


## 3. Data architecture 

The dataset is collected by the Office of Policy and Management and consists of all real estate sales with a sales price of $2000 or greater.
that occure between October 1 (year at time t) and Spetember 30 (year at time t+1) of each year.  For instance, sales from 2020 are from 10/01/2020 to
9/30/2021. For each sale record, the file includes: town, property address, date of sale, property type (residential, apartment, commercial, industrial or vacant land), sales price, and property assessment. 

<img src="https://raw.githubusercontent.com/hsviscarra/RealEstateAnalysis/main/Static_files/Data%20Architecture.png">

### 3.1 Technologies used

- Cloud: Google Cloud (GCP)
- Workflow orchestration: Mage
- Data Warehouse: BigQuery
- Batch processing: DBT
- Dashboard: Google Data Cloud

The pipeline consisted of the following steps:

The pipeline comprised the following steps:

1. Data Extraction: Extracting data from a web page repository.
2. Data Transformation: Converting data types, standardizing column names, and filtering out erroneous entries, such as sold prices listed as zero dollars.
3. Data Loading: Loading the refined data into Google Cloud.
4. Scheduled Execution: Activating the process to run monthly. While updates from the State government occur irregularly, the analysis is performed monthly to capture any changes.
5. Model Building: Employing DBT (Data Build Tool) in the cloud to construct models using SQL.
6. Data Warehousing: Storing the processed data in BigQuery warehouse.
7. Dashboard Development: Utilizing Google Cloud services to develop a compact dashboard for data visualization and analysis purposes.

<br>
<div>
<img src="https://raw.githubusercontent.com/hsviscarra/RealEstateAnalysis/main/Static_files/Dashboard%20example.png">
</div>
<br>
<br>

[Google Report] (https://lookerstudio.google.com/s/hqg23DQPT64)



## 4. How to run the code.

### 4.1. Clone the repository
This repo contains the files of the project. In case of Mage (used for data orchestration) the repor contains a Docker Compose template for getting started with a new Mage project. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/). 

You can start by cloning the repo:

```bash
git clone https://github.com/hsviscarra/RealEstateAnalysis.git [name_of_the_folder]
``

Navigate to the repo:

```bash
cd [name_of_the_folder]
```

### 4.2 Build the container using Docker compose build (This command to build image based on the Docker compose and Docker file provided)

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, you can navigate to http://localhost:6789 in your browser to start building / modifying the pipelines

### 4.3 Changes in io_config.yml -> GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/[name_of_json_payload].json"

### 4.4 Open a google cloud free account to:
   - Create a storage / bucket for storing the data
   - Create a service account (json payload) with owner permissions to connect Mage to GCP

### 4.5 Create an account in DBT cloud and linked to you repo

### 4.6 Open Goolge Data Cloud and connect it to your BigQuery account

## Assistance

1. [Mage Docs](https://docs.mage.ai/introduction/overview): Mage functionality or concepts.
2. [DBT Docs](https://docs.getdbt.com/docs/introduction): DBT documents 
4. [Google Data Studio](https://lookerstudio.google.com/navigation/reporting): Google Data Studio documents




