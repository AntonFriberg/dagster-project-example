"""Example of how to run a Dagster op from normal Python script."""
from jobs.cereal_jobs import complex_op

if __name__ == "__main__":
    result = complex_op.execute_in_process()
