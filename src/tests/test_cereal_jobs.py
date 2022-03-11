"""Example of how to unit-test Dagster pipelines."""
from dagster import ExecuteInProcessResult

from jobs.cereal_jobs import complex_pipeline, hello_cereal_pipeline


def test_hello_cereal_pipeline():
    """Example of a unit test of a simple pipeline."""
    result = hello_cereal_pipeline.execute_in_process()
    assert isinstance(result, ExecuteInProcessResult)
    assert result.success
    assert len(result.output_for_node("hello_cereal")) == 77


def test_complex_pipeline():
    """Example of a unit test of a more complex pipeline."""
    result = complex_pipeline.execute_in_process()
    assert isinstance(result, ExecuteInProcessResult)
    assert result.success
    # inspect individual solid result
    assert len(result.output_for_node("download_cereals")) == 77
    assert result.output_for_node("find_highest_calorie_cereal") == "Strawberry Fruit Wheats"
    assert result.output_for_node("find_highest_protein_cereal") == "Special K"
