"""Collection of Cereal solids"""
import csv

import requests
from dagster import solid


@solid
def hello_cereal(context):
    """Example of a Dagster solid that retrieves data from HTTP source."""
    # Assuming the dataset is in the same directory as this file
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = list(csv.DictReader(lines))

    context.log.info("Found {n_cereals} cereals".format(n_cereals=len(cereals)))

    return cereals


@solid
def download_cereals():
    """Example of a Dagster solid that returns a list of objects."""
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    return list(csv.DictReader(lines))


@solid
def find_highest_calorie_cereal(cereals):
    """Example of a Dagster solid that takes input and produces output."""
    sorted_cereals = list(sorted(cereals, key=lambda cereal: cereal["calories"]))
    return sorted_cereals[-1]["name"]


@solid
def find_highest_protein_cereal(cereals):
    """Example of a Dagster solid that takes input and produces output."""
    sorted_cereals = list(sorted(cereals, key=lambda cereal: cereal["protein"]))
    return sorted_cereals[-1]["name"]


@solid
def display_results(context, most_calories, most_protein):
    """Example of a Dagster solid that takes inputs but does not produce output."""
    context.log.info(f"Most caloric cereal: {most_calories}")
    context.log.info(f"Most protein-rich cereal: {most_protein}")
