# Deezer Chart Pipeline

A small ETL pipeline that pulls the current top tracks from the public [Deezer Chart API](https://api.deezer.com/chart), validates them with Pydantic, cleans them with Polars, and saves the result as a Parquet file.

```
Deezer API  ->  Validate (Pydantic)  ->  Clean (Polars)  ->  Parquet
```

## Features

- **Extract** the top tracks from `https://api.deezer.com/chart` (the `tracks` section).
- **Validate** each track against a typed schema, so malformed records are caught early.
- **Clean** the data with Polars (normalized text, flattened artist, renamed columns, filtering, de-duplication).
- **Load** the cleaned data to `data/processed/tracks.parquet`.
- **Test** the cleaning logic with Pytest.

## Project Structure

```
.
├── data/
│   └── processed/
│       └── tracks.parquet        # pipeline output (generated)
├── src/
│   ├── __init__.py
│   ├── understanding.py          # explores the API's JSON structure
│   ├── data_validator.py         # Pydantic models (Artist, Track)
│   ├── api_validation.py         # fetches the API and validates the tracks
│   └── clean_dataframe.py        # clean_data(): Polars cleaning logic
├── tests/
│   ├── __init__.py
│   └── test_clean_data.py        # Pytest tests for clean_data()
├── main.py                       # runs the full pipeline
├── pytest.ini                    # sets pythonpath so `src` is importable
├── requirements.txt
└── README.md
```

## How It Works

### 1. Understanding the API (`src/understanding.py`)
A exploration script that prints the structure of the Deezer chart response. The response has five sections (`tracks`, `albums`, `artists`, `playlists`, `podcasts`), each with 10 items. This project uses **tracks** only.

Selected fields: `id`, `title`, `link`, `duration`, `rank`, `preview`, `type`, and the artist's `name`.

### 2. Validation (`src/data_validator.py`, `src/api_validation.py`)
Pydantic models define the expected shape of each record:

| Model    | Fields                                                                                      |
|----------|---------------------------------------------------------------------------------------------|
| `Artist` | `id: int`, `name: str`                                                                      |
| `Track`  | `id: int`, `title: str`, `link: str \| None`, `duration: int`, `rank: int`, `preview: str \| None`, `artist: Artist`, `type: str` |

`api_validation.py` calls the API, handles HTTP and network errors, and validates every track against the `Track` model. Errors are logged.

### 3. Cleaning (`src/clean_dataframe.py`)
`clean_data(df)` takes a Polars DataFrame and returns a cleaned one. Based on the tests, it:

- lowercases `title`
- extracts the artist name into `artist_name` (lowercased)
- renames `duration` to `duration_seconds`
- filters rows that don't match the expected link/preview rules
- removes duplicate tracks

### 4. Pipeline (`main.py`)
Runs fetch -> validate -> clean, then writes the result to `data/processed/tracks.parquet`.

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
git clone <your-repo-url>
cd <your-repo-folder>

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### Run the pipeline

Run from the project root, because the code imports from `src`:

```bash
python main.py
```

The cleaned data is printed to the console and saved to `data/processed/tracks.parquet`.

### Explore the API structure

```bash
python src/understanding.py
```

### Read the output

```python
import polars as pl

df = pl.read_parquet("data/processed/tracks.parquet")
print(df)
```

## Testing

```bash
pytest
```

`pytest.ini` sets `pythonpath = .`, so `from src... import ...` works in tests. Test files must be named `test_*.py` for Pytest to find them.

## Output Schema

| Column             | Description                          |
|--------------------|--------------------------------------|
| `id`               | Deezer track ID                      |
| `title`            | Track title (lowercase)              |
| `artist_name`      | Artist name (lowercase)              |
| `duration_seconds` | Track length in seconds              |
| `rank`             | Deezer popularity rank               |
| `link`             | URL of the track on Deezer           |
| `preview`          | URL of the 30-second preview         |

## Tech Stack

- [Requests](https://requests.readthedocs.io/) for HTTP calls
- [Pydantic](https://docs.pydantic.dev/) for data validation
- [Polars](https://pola.rs/) for data cleaning
- [Pytest](https://docs.pytest.org/) for testing

## Possible Improvements

- Add the other API sections (albums, artists, playlists, podcasts)
- Schedule the pipeline (cron, Airflow, or GitHub Actions)
- Append runs to the Parquet file with a timestamp to keep history
- Add more tests for edge cases (null links, duplicates, empty data)
- Add a CLI option for the output path

## Data Source

Data comes from the [Deezer API](https://developers.deezer.com/api). Please follow Deezer's terms of use.
