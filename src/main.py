"""Example of how to run a Dagster pipeline from normal Python script."""
from dagster import execute_pipeline

from pipelines.cereal_pipelines import complex_pipeline

if __name__ == "__main__":
    result = execute_pipeline(complex_pipeline)
