import pytest


@pytest.mark.smoke
def test_cat_says(generate_cats):
    cat = generate_cats
    say = cat.say()

    assert say == "Meow!"

@pytest.mark.car
def test_car_engine(generate_car):
    car = generate_car
    engine_status = car.get_engine()

    assert engine_status is False

    engine_status = car.set_engine()

    assert engine_status is True

    engine_status = car.set_engine()

    assert engine_status is False
