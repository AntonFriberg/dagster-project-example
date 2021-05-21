"""Collection of Cereal repositories"""
from dagster import repository

from pipelines.cereal_pipelines import complex_pipeline, hello_cereal_pipeline
from schedules.cereal_schedules import every_weekday_9am


@repository
def hello_cereal_repository():
    """Collection of cereal pipelines and other definitions used by Dagster."""
    return {
        "pipelines": {
            "hello_cereal_pipeline": lambda: hello_cereal_pipeline,
            "complex_pipeline": lambda: complex_pipeline,
        },
        "schedules": {"every_weekday_9am": lambda: every_weekday_9am},
    }
