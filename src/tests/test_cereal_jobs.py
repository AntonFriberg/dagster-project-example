"""Example of how to unit-test Dagster ops."""
from dagster import ExecuteInProcessResult

from jobs.cereal_jobs import complex_op, hello_cereal_op


def test_hello_cereal_op():
    """Example of a unit test of a simple op."""
    result = hello_cereal_op.execute_in_process()
    assert isinstance(result, ExecuteInProcessResult)
    assert result.success
    assert len(result.output_for_node("hello_cereal")) == 77


def test_complex_op():
    """Example of a unit test of a more complex op."""
    result = complex_op.execute_in_process()
    assert isinstance(result, ExecuteInProcessResult)
    assert result.success
    # inspect individual ops result
    assert len(result.output_for_node("download_cereals")) == 77
    assert result.output_for_node("find_highest_calorie_cereal") == "Strawberry Fruit Wheats"
    assert result.output_for_node("find_highest_protein_cereal") == "Special K"
