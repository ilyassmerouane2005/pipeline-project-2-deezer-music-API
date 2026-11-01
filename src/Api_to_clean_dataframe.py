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
    pl.col('title').str.strip_chars().str.to_lowercase().alias('title') ,
    pl.col('artist').struct.field('name').str.strip_chars().str.to_lowercase().alias('artist_name') ,
    pl.col('duration').alias('duration in seconds') ,  
    'rank' ,
    pl.col('preview').alias('preview_url') ,
    pl.col('link').alias('track_link_url')
])
print(df)