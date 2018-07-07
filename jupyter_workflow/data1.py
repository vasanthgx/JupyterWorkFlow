import os
from urllib.request import urlretrieve
import pandas as pd
fremont_url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv'
def  get_fremont_data(filename = 'Fremont.csv', url  = fremont_url, force_download = False):
	if force_download or not os.path.exists(filename):
		urlretrieve(url, filename)
	data = pd.read_csv('Fremont.csv',  index_col= 'Date')
	try:
		data.index = pd.to_datetime(data.index, format = '%m/%d/%Y %H:%M:%S %p')
	except TypeError:
    data.index = pd.to_datetime(data.index)
    
    
	data.columns = ['West' , 'East']
	data['Total'] = data["East"] + data["West"]
	return data
