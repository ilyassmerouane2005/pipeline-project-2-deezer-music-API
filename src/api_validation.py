import requests 
from pydantic import ValidationError as PydanticValidationError
from src.data_validator import Track
import polars as pl
import logging
logging.basicConfig(level=logging.INFO , format='%(asctime)s - %(levelname)s - %(message)s' , datefmt='%Y-%m-%d %H:%M:%S')

try :
    url = 'https://api.deezer.com/chart'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()  # Raise an exception for HTTP errors
    logging.info("API request successful.")
except requests.exceptions.RequestException as e:
    logging.error(f"Error occurred while making the API request: {e}")
    raise SystemExit(e)

try :
    tracks = response['tracks']['data']
    valid_tracks = [Track(**track) for track in tracks]
    logging.info("Tracks data validated successfully.")
except KeyError as e:
    logging.error(f"KeyError occurred while accessing tracks data or: {e}")
except PydanticValidationError as e:
    logging.error(f"An unexpected error occurred while validating tracks data: {e}")