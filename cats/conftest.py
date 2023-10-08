import pytest
from cats import Cats
from car import Car


@pytest.fixture()
def generate_cats():
    return Cats()

@pytest.fixture()
def generate_car():
    return Car()
