"""Collection of Cereal pipelines"""
from dagster import job

from ops.cereal_ops import (
    display_results,
    download_cereals,
    find_highest_calorie_cereal,
    find_highest_protein_cereal,
    hello_cereal,
)

# pylint: disable=no-value-for-parameter


@job
def hello_cereal_pipeline():
    """Example of a simple Dagster Pipeline."""
    hello_cereal()


@job
def complex_pipeline():
    """Example of a more complex Dagster Pipeline."""
    cereals = download_cereals()
    display_results(
        most_calories=find_highest_calorie_cereal(cereals),
        most_protein=find_highest_protein_cereal(cereals),
    )
