"""Definitions that provide Dagster code locations."""

from dagster import Definitions

from dagster_example.assets.product_catalog import products, catalog_with_most_products, highest_price_product

defs = Definitions(
    assets=[products, catalog_with_most_products, highest_price_product],
)
