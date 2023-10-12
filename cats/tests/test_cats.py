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

@pytest.mark.car
    def test_car_brakes(generate_car):
        car = generate_car
        brakes_status = car.get_brakes()

        assert brakes_status is False

        brakes_status = car.drive()

        assert brakes_status is True

        brakes_status = car.stop()

        assert brakes_status is False
        
