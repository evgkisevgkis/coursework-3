from coursework_3.utils import *


def test_load_data():
    assert type(load_data("operations.json")) == list
