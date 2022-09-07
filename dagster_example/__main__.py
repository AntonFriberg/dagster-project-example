"""Example of how to run a Dagster op from normal Python script."""
from dagster_example.jobs import complex_job

if __name__ == "__main__":
    result = complex_job.execute_in_process()
