from solids.cereal_solids import (
    download_cereals,
    display_results,
    find_highest_calorie_cereal,
    find_highest_protein_cereal,
    hello_cereal,
)

from dagster import pipeline

# pylint: disable=no-value-for-parameter


@pipeline
def hello_cereal_pipeline():
    hello_cereal()


@pipeline
def complex_pipeline():
    cereals = download_cereals()
    display_results(
        most_calories=find_highest_calorie_cereal(cereals),
        most_protein=find_highest_protein_cereal(cereals),
    )
