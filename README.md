<div>
  <img src="https://raw.githubusercontent.com/hsviscarra/RealEstateAnalysis/main/Static_files/retail_image.jpeg" style="width: 100%; height: 500px;">
</div>

## REAL STATE DATA ANALYSIS - CONNECTICUT STATE

Welcome to Retail Data Analysis Repository 




## 1. Objective

The objective is to analyze the real estate price evolution of the propoerties sold in Connecticut from 2001 to 2021. The analysis will be perfomed by town and property type.


## 2. Problem statement

Knowing about the evolution of prices may help investors and individual home-owners to make better decisions. 
For investors to focus their effort on markets that are experiencing an increase in the prices to maximize their profits.
For home-owners which great part of their wealth is invested in their own homes, to buy in areas with value appreciation.

As an illustrative example, this project uses the Connecticut property sales dataset:
[Data source](https://catalog.data.gov/dataset/real-estate-sales-2001-2018)


## 3. Data architecture 

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
<img src="https://raw.githubusercontent.com/hsviscarra/RealEstateAnalysis/main/Static_files/Dashboard%20example.png"
</div>
<br>
<br>


## 4. Techonologies used
- Cloud: Google Cloud (GCP)
- Workflow orchestration: Mage
- Data Warehouse: BigQuery
- Batch processing: DBT
- Dashboard: Google Data Cloud

## 5. How to run the code.
1. Clone the repository
2. Open a google cloud free account to:
   - Create a storage / bucket to dump the data
   - Create a service account json payload with owner permissions to connect mage with GCP
3. Docker compose build (This command to build image based on the Docker compose and Docker file provided)
4. Docker compose up (To run the services)
5. Changes in io_config.yml -> GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/[name_of_json_payload].json"
6. Save and run the pipeline.
7. Create an accouunt in DBT cloud and linked to you repo
8. Make the adjustements in the models
9. DBT Build
10. Open Goolge Data Cloud and connect it to your BigQuery account
11. Perform changes in the dashboard
