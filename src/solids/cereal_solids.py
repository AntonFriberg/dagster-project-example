import csv

import requests
from dagster import solid


@solid
def hello_cereal(context):
    # Assuming the dataset is in the same directory as this file
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]

    context.log.info(
        "Found {n_cereals} cereals".format(n_cereals=len(cereals))
    )

    return cereals


@solid
def download_cereals(_):
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    return [row for row in csv.DictReader(lines)]


@solid
def find_highest_calorie_cereal(_, cereals):
    sorted_cereals = list(sorted(cereals, key=lambda cereal: cereal["calories"]))
    return sorted_cereals[-1]["name"]


@solid
def find_highest_protein_cereal(_, cereals):
    sorted_cereals = list(sorted(cereals, key=lambda cereal: cereal["protein"]))
    return sorted_cereals[-1]["name"]


@solid
def display_results(context, most_calories, most_protein):
    context.log.info(f"Most caloric cereal: {most_calories}")
    context.log.info(f"Most protein-rich cereal: {most_protein}")
