import pytest


@pytest.mark.smoke
def test_cat_says(generate_cats):
    cat = generate_cats
    say = cat.say()

    assert say == "Meow!"
