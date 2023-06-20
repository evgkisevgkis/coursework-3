from coursework_3.utils import *


def test_load_data():
    assert type(load_data("operations.json")) == list


def test_sort_data():
    assert len(sort_data(load_data("operations.json"))) == 5


def test_prepare_data():
    assert type(prepare_data(sort_data(load_data("operations.json")))) == str
