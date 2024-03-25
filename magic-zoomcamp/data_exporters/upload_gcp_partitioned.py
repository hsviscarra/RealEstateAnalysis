import pyarrow as pa 
import pyarrow.parquet as pq 
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/retaildataanalysis-52f35ed8b7bf.json"

bucket_name = 'us_real_state_dataset'
project_id = 'retaildataanalysis'
table_name = "connecticut_realestate_data"

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    data['Date'] = data['Date Recorded'].dt.year
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['Date'],
        filesystem=gcs
    )