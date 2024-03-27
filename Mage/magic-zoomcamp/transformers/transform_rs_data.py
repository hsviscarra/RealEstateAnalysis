import numpy as np
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data = data.loc[data['sale_amount'] !=0 ]
    data['sales_ratio'] = data['sales_ratio'].replace(0, np.nan)
    data['date_recorded'] = pd.to_datetime(data['date_recorded'], unit='s')
    
    return data


@test
def test_output(output, *args) -> None:

    assert output is not None, 'The output is undefined'
    assert output['sale_amount'].isin([0]).sum() == 0, 'There are sales with 0 USD'
