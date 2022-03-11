"""Collection of Cereal solids"""
import csv

import requests
from dagster import op, get_dagster_logger


@op
def hello_cereal():
    """Example of a Dagster op that retrieves data from HTTP source."""
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = list(csv.DictReader(lines))
    get_dagster_logger().info(f"Found {len(cereals)} cereals")
    return cereals


@op
def download_cereals():
    """Example of a Dagster op that returns a list of objects."""
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    return list(csv.DictReader(lines))


@op
def find_highest_calorie_cereal(cereals):
    """Example of a Dagster op that takes input and produces output."""
    sorted_by_calorie = list(sorted(cereals, key=lambda cereal: cereal["calories"]))
    get_dagster_logger().info(
        f'{sorted_by_calorie[-1]["name"]} is the cereal that contains the most calories'
    )
    return sorted_by_calorie[-1]["name"]


@op
def find_highest_protein_cereal(cereals):
    """Example of a Dagster op that takes input and produces output."""
    sorted_by_protein = list(sorted(cereals, key=lambda cereal: cereal["protein"]))
    get_dagster_logger().info(
        f'{sorted_by_protein[-1]["name"]} is the cereal that contains the most protein'
    )
    return sorted_by_protein[-1]["name"]


@op
def display_results(most_calories, most_protein):
    """Example of a Dagster op that takes inputs but does not produce output."""
    logger = get_dagster_logger()
    logger.info(f"Most caloric cereal: {most_calories}")
    logger.info(f"Most protein-rich cereal: {most_protein}")
