"""Collection of Product ops"""

import csv
from typing import List

from dagster import Nothing, get_dagster_logger, op

PRODUCT_DATA_PATH = "dagster_example/data/product_data.csv"


@op
def load_products() -> List[dict]:
    """Dagster op to load products from a local CSV file."""
    with open(PRODUCT_DATA_PATH, newline="") as csvfile:
        products = list(csv.DictReader(csvfile))
    get_dagster_logger().info(f"Found {len(products)} products")
    return products


@op
def get_products_by_catalog(products: List[dict], catalog: str) -> List[dict]:
    """Return products filtered by catalog name."""
    filtered = [p for p in products if p.get("catalog", "").lower() == catalog.lower()]
    get_dagster_logger().info(f"Found {len(filtered)} products in catalog '{catalog}'")
    return filtered


@op
def get_top_3_products_by_price(products: List[dict]) -> List[dict]:
    """Return the top 3 products by price."""
    sorted_by_price = sorted(products, key=lambda p: float(p.get("price", 0)), reverse=True)
    top3 = sorted_by_price[:3]
    get_dagster_logger().info(f"Top 3 products by price: {[p.get('name') for p in top3]}")
    return top3


@op
def get_product_counts_per_catalog(products: List[dict]) -> dict:
    """Return a dictionary with catalog names as keys and product counts as values."""
    counts = {}
    for p in products:
        catalog = p.get("catalog", "Unknown")
        counts[catalog] = counts.get(catalog, 0) + 1
    get_dagster_logger().info(f"Product counts per catalog: {counts}")
    return counts


@op
def display_results(top3_products: str, per_catalog: str) -> Nothing:
    logger = get_dagster_logger()
    logger.info(f"Top 3 products: {top3_products}")
    logger.info(f"Products per catalog: {per_catalog}")