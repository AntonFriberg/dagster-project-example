"""Example of how to unit-test Dagster pipelines."""
from dagster import PipelineExecutionResult, execute_pipeline

from pipelines.cereal_pipelines import complex_pipeline, hello_cereal_pipeline


def test_hello_cereal_pipeline():
    """Example of a unit test of a simple pipeline."""
    res = execute_pipeline(hello_cereal_pipeline)
    assert res.success
    assert len(res.result_for_solid("hello_cereal").output_value()) == 77


def test_complex_pipeline():
    """Example of a unit test of a more complex pipeline."""
    res = execute_pipeline(complex_pipeline)
    # return type is PipelineExecutionResult
    assert isinstance(res, PipelineExecutionResult)
    assert res.success
    # inspect individual solid result
    assert len(res.output_for_solid("download_cereals")) == 77
    assert res.output_for_solid("find_highest_calorie_cereal") == "Strawberry Fruit Wheats"
    assert res.output_for_solid("find_highest_protein_cereal") == "Special K"
