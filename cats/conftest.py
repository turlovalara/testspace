import pytest
from cats import Cats
from cats import AminalFactory
from tests.core.steps import *


@pytest.fixture()
def generate_cats():
    return Cats()


@pytest.fixture()
def generate_animal():
    return AminalFactory()