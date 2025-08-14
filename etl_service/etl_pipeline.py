import pandas as pd
from db import get_connection, init_db
from logger import get_logger

logger = get_logger()

def normalize_dates(df, date_columns):
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce', utc=True)
        df[col] = df[col].dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    return df

def normalize_product_names(df):
    df['name'] = df['name'].astype(str).str.strip().str.title()
    return df

def fill_empty_prices_with_average(df):
    avg_price = df['price'].mean(skipna=True)
    df['price'] = df['price'].fillna(avg_price)
    return df

def run_etl(catalog_csv, product_csv):
    try:
        logger.info("Starting ETL process...")

        # Extract
        logger.info(f"Reading catalogs CSV: {catalog_csv}")
        catalogs_df = pd.read_csv(catalog_csv)
        logger.info(f"Reading products CSV: {product_csv}")
        products_df = pd.read_csv(product_csv)

        # Transform
        catalogs_df.columns = [col.strip().lower() for col in catalogs_df.columns]
        products_df.columns = [col.strip().lower() for col in products_df.columns]

        catalogs_df = normalize_dates(catalogs_df, ['created_at', 'updated_at'])
        products_df = normalize_dates(products_df, ['created_at', 'updated_at'])
        products_df = normalize_product_names(products_df)
        products_df['price'] = pd.to_numeric(products_df['price'], errors='coerce')
        products_df = fill_empty_prices_with_average(products_df)

        # Load
        init_db()
        conn = get_connection()
        catalogs_df.to_sql('catalogs', conn, if_exists='replace', index=False)
        products_df.to_sql('products', conn, if_exists='replace', index=False)
        conn.close()

        logger.info("ETL completed successfully.")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        logger.error(f"CSV file is empty: {e}")
        raise
    except Exception as e:
        logger.exception(f"Unexpected error during ETL: {e}")
        raise
