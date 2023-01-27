"""Example of how to unit-test Dagster jobs."""
from dagster import ExecuteInProcessResult

from dagster_example.jobs import complex_job, hello_cereal_job

from . import MOCKED_CEREAL_LEN


def test_hello_cereal_job():
    """Example of a unit test of a simple job."""
    result = hello_cereal_job.execute_in_process()
    assert isinstance(result, ExecuteInProcessResult)
    assert result.success
    assert len(result.output_for_node("hello_cereal")) == MOCKED_CEREAL_LEN


def test_complex_job():
    """Example of a unit test of a more complex job."""
    result = complex_job.execute_in_process()
    assert isinstance(result, ExecuteInProcessResult)
    assert result.success
    # inspect individual ops result
    assert len(result.output_for_node("download_cereals")) == MOCKED_CEREAL_LEN
    assert result.output_for_node("find_highest_calorie_cereal") == "Strawberry Fruit Wheats"
    assert result.output_for_node("find_highest_protein_cereal") == "Special K"
