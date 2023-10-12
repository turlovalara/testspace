from pytest_bdd import (given, when, then, parsers)
from .store import Store


store = Store()

@given(parsers.re('birth of a "(?P<animal_type>[^\"]*)" and call "(?P<animal_name>[^\"]*)"'))
def birth_of_a_dog(generate_animal, animal_type, animal_name):
    animal = generate_animal.create_animal(animal_type=animal_type, name=animal_name)
    store.set_item(animal_name, animal)
    print(f'\nSTEP birth of a "{animal_type}" and call "{animal_name}" save as "{animal_name}" PASS')


@when(parsers.re('"(?P<animal_name>[^\"]*)" says save it as "(?P<save_name>[^\"]*)"'))
def birth_of_a_dog(animal_name, save_name):
    animal = store.get_item(animal_name)
    animal_said = animal.say()
    store.set_item(save_name, animal_said)
    print(f'\nSTEP "{animal_name}" says "{animal_said}" and save as "{save_name}" PASS')


@then(parsers.re('assert animal (?P<animal_action>[^\"]*) "(?P<sound>[^\"]*)"'))
def birth_of_a_dog(animal_action, sound):
    animal_said = store.get_item(animal_action)

    try:
        assert animal_said == sound
    except:
        raise AssertionError(f'"{animal_said}" NOT EQUAL "{sound}"')

    print(f'\nSTEP assert animal "{animal_said}" EQUAL "{sound}" PASS')
