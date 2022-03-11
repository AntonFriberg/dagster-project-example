"""Example of how to run a Dagster pipeline from normal Python script."""
from pipelines.cereal_pipelines import complex_pipeline

if __name__ == "__main__":
    result = complex_pipeline.execute_in_process()
