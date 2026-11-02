from api_validation import valid_tracks 
import polars as pl
pl.Config.set_tbl_cols(-1)
df_tracks = pl.DataFrame(valid_tracks)
print(f"Tracks DataFrame from the validated data of the API response:{df_tracks}")

def clean_dataframe(df: pl.DataFrame) -> pl.DataFrame:
    df_clean_tracks = df_tracks.select([
        pl.col('id') ,
        pl.col('title').str.strip_chars('').str.to_lowercase() ,
        pl.col('artist').struct.field('name').str.strip_chars('').str.to_lowercase().alias('artist_name') ,
        pl.col('duration').alias('duration_seconds') ,
        pl.col('rank') ,
        pl.col('link').str.strip_chars('') ,
        pl.col('preview').str.strip_chars('') 
    ]).sort('rank' , descending=True)
    return df_clean_tracks