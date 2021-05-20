from typing import OrderedDict
from dagster import execute_pipeline, execute_solid

from solids.cereal_solids import (
    find_highest_protein_cereal,
    find_highest_calorie_cereal,
    display_results,
    download_cereals,
    hello_cereal,
)

TEST_CEREALS = [
    OrderedDict([("name", "All-Bran"), ("calories", 70), ("protein", 4)]),
    OrderedDict([("name", "Corn Flakes"), ("calories", 100), ("protein", 2)]),
    OrderedDict([("name", "Special K"), ("calories", 110), ("protein", 6)]),
]


def test_hello_cereal_solid():
    res = execute_solid(hello_cereal)
    assert res.success
    assert len(res.output_value()) == 77


def test_cereal_solid_download_cereal():
    res = execute_solid(download_cereals)
    assert res.success
    assert len(res.output_value()) == 77


def test_cereal_solid_find_highest_protein_cereal():
    res = execute_solid(
        find_highest_protein_cereal, input_values={"cereals": TEST_CEREALS}
    )
    assert res.success
    assert res.output_value() == "Special K"


def test_cereal_solid_find_highest_calorie_cereal():
    res = execute_solid(
        find_highest_calorie_cereal, input_values={"cereals": TEST_CEREALS}
    )
    assert res.success
    assert res.output_value() == "Special K"


def test_cereal_solid_display_result(mocker):
    test_inputs = {
        "most_calories": "Special K",
        "most_protein": "Special K",
    }
    res = execute_solid(display_results, input_values=test_inputs)
    assert res.success
