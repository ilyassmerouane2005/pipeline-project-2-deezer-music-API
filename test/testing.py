import pytest 
import polars as pl
from src.clean_dataframe import clean_data
def test_clean_data():
    mock_data = pl.DataFrame({
        'id' : [3812345 , 12345 , 123457] ,
        'title' : ['The Great Gatsby' , 'To Kill a Mockingbird' , '1984'] ,
        'artist' : [{'name':'Ilyass'} , {'name':'houssam'} , {'name':'reda'}] ,
        'duration' : [200 , 150 , 230] ,
        'rank' : [9994000 , 1233 , 13333323] ,
        'link' : ['https://www.deezer.com/book/show/4671.The_Great_Gatsby' , 'https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird' , 'https://www.goodreads.com/book/show/5470.1984'] ,
        'preview' : ['preview.dzcdn.net' , 'www.python.com' , 'www.preview.com']
    })
    results = clean_data(mock_data)
    assert results.height == 1
    assert results['title'][0] == 'the great gatsby'
    assert results['artist_name'][0] == 'ilyass'
    assert results['duration_seconds'][0] == 200
