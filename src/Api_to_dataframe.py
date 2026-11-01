"""
the idea from this scripts is to understand the api structure and extract the useful data from the api and convert it into a dataframe using polars library.
"""
import requests 
import polars as pl
import json
pl.Config.set_tbl_cols(-1)
url = 'https://api.deezer.com/chart'
data = requests.get(url).json()
print('Keys in the response:', data.keys())
print('Keys in the tracks :', data['tracks'].keys()) 
print('Keys in the tracks data:', data['tracks']['data'][0].keys())
df = pl.DataFrame(data['tracks']['data'])
df = df.select([
    'id' ,
    'title' ,
    'link' ,  
    'duration' ,
    'rank' ,
    'preview' ,
    'position' , 
    pl.col('artist').struct.field('name').alias('artist_name')
])