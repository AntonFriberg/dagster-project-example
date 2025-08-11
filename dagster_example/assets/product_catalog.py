"""Collection of Catalog and Product assets"""

import csv
from typing import List, Dict

from dagster import asset, get_dagster_logger

CATALOGS_CSV_PATH = "dagster_example/data/catalog_data.csv"
PRODUCTS_CSV_PATH = "dagster_example/data/product_data.csv"


def read_csv_to_dicts(file_path: str) -> List[Dict]:
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        return list(csv.DictReader(csvfile))


@asset
def catalogs() -> List[Dict]:
    """Asset representing a list of catalogs."""
    catalog_list = read_csv_to_dicts(CATALOGS_CSV_PATH)
    get_dagster_logger().info(f"Found {len(catalog_list)} catalogs")
    return catalog_list


@asset
def products() -> List[Dict]:
    """Asset representing a list of products."""
    product_list = read_csv_to_dicts(PRODUCTS_CSV_PATH)
    get_dagster_logger().info(f"Found {len(product_list)} products")
    return product_list


@asset
def highest_price_product(product_list: List[Dict] = products()) -> str:
    """Asset representing the product with the highest price."""
    sorted_by_price = sorted(product_list, key=lambda p: float(p["price"]))
    get_dagster_logger().info(
        f'{sorted_by_price[-1]["name"]} is the product with the highest price'
    )
    return sorted_by_price[-1]["name"]


@asset
def catalog_with_most_products(product_list: List[Dict] = products(), catalog_list: List[Dict] = catalogs()) -> str:
    """Asset representing the catalog with the most products."""
    from collections import Counter
    catalog_counts = Counter(p["catalog_id"] for p in product_list)
    if not catalog_counts:
        return ""
    most_common_catalog_id, _ = catalog_counts.most_common(1)[0]
    catalog = next((c for c in catalog_list if c["id"] == most_common_catalog_id), None)
    catalog_name = catalog["name"] if catalog else ""
    get_dagster_logger().info(
        f'{catalog_name} has the most products'
    )
    return catalog_name
