from src.api_validation import valid_tracks
from src.clean_dataframe import clean_data
import polars as pl

def run_pipeline ():
    df = pl.DataFrame(valid_tracks)
    data = clean_data(df)
    print(data)
    return data.write_parquet('data/processed/tracks.parquet')

if __name__ == '__main__' :
    run_pipeline()