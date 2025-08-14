import streamlit as st
import pandas as pd
from db import get_connection
from etl_pipeline import run_etl
from logger import get_logger

logger = get_logger()

st.title("Simple ETL Pipeline")

# --- ETL ---
if st.button("Start ETL"):
    try:
        run_etl("data/catalogs.csv", "data/products.csv")
        st.success("✅ ETL completed! Data saved to SQLite.")
    except FileNotFoundError:
        st.error("❌ CSV file not found. Please check the file path.")
    except Exception as e:
        st.error(f"❌ ETL failed: {str(e)}")
        logger.error(f"ETL failed: {e}")

# --- Show Results ---
if st.button("Show Results"):
    try:
        conn = get_connection()
        query = """
        SELECT p.product_id,
               p.name AS product_name,
               p.price,
               c.name AS catalog_name,
               p.created_at,
               p.updated_at
        FROM products p
        LEFT JOIN catalogs c
        ON p.catalog_id = c.catalog_id
        """
        products = pd.read_sql(query, conn)
        catalogs = pd.read_sql("SELECT * FROM catalogs", conn)
        conn.close()

        st.subheader("Catalogs")
        st.dataframe(catalogs)

        st.subheader("Products (with Catalog Names)")
        st.dataframe(products)

    except Exception as e:
        st.error(f"❌ Failed to load results: {str(e)}")
        logger.error(f"Show results failed: {e}")

# --- Queries Section ---
st.header("📊 Data Queries")
