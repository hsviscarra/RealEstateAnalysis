if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import numpy as np

@transformer
def transform(data, *args, **kwargs):
    data_processed = data.drop(columns=['Non Use Code', 'Assessor Remarks', 'OPM remarks', 'Location'])
    data_processed = data_processed
    data_processed[['Assessed Value', 'Sale Amount', 'Sales Ratio']] = data_processed[['Assessed Value', 'Sale Amount', 'Sales Ratio']].replace(0, np.nan)
    return data_processed


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output["Sale Amount"].isin([0]).sum()==0, 'There are sales amounts equal to zero'
