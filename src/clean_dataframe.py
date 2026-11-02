import polars as pl
pl.Config.set_tbl_cols(-1)
def clean_data(df: pl.DataFrame) -> pl.DataFrame:
        df_clean = ( 
            df.filter(
                pl.col('link').str.contains('www.deezer.com') ,
                pl.col('preview').str.contains('preview.dzcdn') 
        )
        .select([
            pl.col('id') ,
            pl.col('title').str.strip_chars().str.to_lowercase() ,
            pl.col('artist').struct.field('name').str.strip_chars().str.to_lowercase().alias('artist_name') ,
            pl.col('duration').alias('duration_seconds') ,
            pl.col('rank') ,
            pl.col('link').str.strip_chars() ,
            pl.col('preview').str.strip_chars() 
    ])).sort('rank' , descending=True)
        return pl.DataFrame(df_clean)