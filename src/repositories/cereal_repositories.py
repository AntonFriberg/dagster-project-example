"""Collection of Cereal repositories"""
from dagster import repository

from jobs import complex_job, hello_cereal_job
from schedules.cereal_schedules import every_weekday_9am


@repository
def hello_cereal_repository():
    """Collection of cereal jobs and other definitions used by Dagster."""
    return [complex_job, hello_cereal_job, every_weekday_9am]
