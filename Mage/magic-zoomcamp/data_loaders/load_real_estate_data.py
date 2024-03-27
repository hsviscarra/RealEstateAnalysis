import io
import pandas as pd
import requests

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

    rs_dtypes = {
        "Serial Number": int,
        "List Year": int,
        "Town": str,
        "Address": str,
        "Assesed Value": float,
        "Sale Amount": float,
    }

    parse_dates = ["Date Recorded"] 

    data = pd.read_csv(url, dtype=rs_dtypes, parse_dates=parse_dates)
    data.columns = [col.replace(" ", "_").lower() for col in data.columns]
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
