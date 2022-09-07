"""Collection of Dagster repositories"""
from dagster import repository

from dagster_example.jobs import complex_job, hello_cereal_job
from dagster_example.schedules import every_weekday_9am


@repository
def dagster_examples():
    """Collection of example jobs and schedules used by Dagster."""
    return [complex_job, hello_cereal_job, every_weekday_9am]
