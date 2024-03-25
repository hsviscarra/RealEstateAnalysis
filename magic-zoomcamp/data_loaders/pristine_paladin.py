import io
import pandas as pd
import requests
import numpy as np

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://data.ct.gov/api/views/5mzw-sjtu/rows.csv?accessType=DOWNLOAD'

    properties_dtypes = {
    "Serial Number": str,
    "List Year": pd.Int64Dtype(),
    "Town":str,
    "Address":str,
    "Assessed Value": float,
    "Sale Amount": float,
    "Sales Ratio": float,
    "Property Type": str,
    "Residential Type": str,
    "Non Use Code": str,
    "Assessor Remarks": str,
    "OPM remarks": str,
    "Location": str,
}

    parse_dates = ["Date Recorded"]
    
    return pd.read_csv(url, sep=',', dtype=properties_dtypes, parse_dates=parse_dates)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'