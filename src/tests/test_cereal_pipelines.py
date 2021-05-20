from dagster import execute_pipeline, PipelineExecutionResult

from pipelines.cereal_pipelines import hello_cereal_pipeline, complex_pipeline


def test_hello_cereal_pipeline():
    res = execute_pipeline(hello_cereal_pipeline)
    assert res.success
    assert len(res.result_for_solid("hello_cereal").output_value()) == 77


def test_complex_pipeline():
    res = execute_pipeline(complex_pipeline)
    # return type is PipelineExecutionResult
    assert isinstance(res, PipelineExecutionResult)
    assert res.success
    # inspect individual solid result
    assert len(res.output_for_solid("download_cereals")) == 77
    assert res.output_for_solid("find_highest_calorie_cereal") == "Strawberry Fruit Wheats"
    assert res.output_for_solid("find_highest_protein_cereal") == "Special K"
