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
https://data.wa.gov/api/views/https://data.wa.gohttps://data.wa.gohttps://data.wa.gohttps://data.wa.gohttps://data.wa.gohttps://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOADv/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOADv/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOADv/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOADv/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOADv/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOADf6w7-q2d2/rows.csv?accessType=DOWNLOADhttps://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOADov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD
    """
    url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
    response = requests.get(url)

    ev_datatypes = {
    'VIN (1-10)':str,
    'County':str,
    'City':str,
    'State':str,
    'Postal Code':str,
    'Model Year':str,
    'Make':str,
    'Model':str, 
    'Electric Vehicle Type':str,
    'Clean Alternative Fuel Vehicle (CAFV) Eligibility':str, 
    'Electric Range':pd.Int64Dtype(),
    'Base MSRP':pd.Int64Dtype(), 
    'Legislative District':str, 
    'DOL Vehicle ID':str,
    'Vehicle Location':str, 
    'Electric Utility':str, 
    '2020 Census Tract':str   
}

    df = pd.read_csv(io.StringIO(response.text), sep=',', dtype=ev_datatypes)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
