from dagster import repository

from pipelines.cereal_pipelines import hello_cereal_pipeline, complex_pipeline
from schedules.cereal_schedules import every_weekday_9am


@repository
def hello_cereal_repository():
    return {
        "pipelines": {
            "hello_cereal_pipeline": lambda: hello_cereal_pipeline,
            "complex_pipeline": lambda: complex_pipeline,
        },
        "schedules": {"every_weekday_9am": lambda: every_weekday_9am},
    }
