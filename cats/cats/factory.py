class Dogs:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name", "Bob")

    def __str__(self):
        return f"Name is {self.name}"

    def say(self):
        return "Gav!"

class Cats:

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name", "Bob")

    def __str__(self):
        return f"Name is {self.name}"

    def say(self):
        return "Meow!"

class AminalFactory:

    def create_animal(self, animal_type, name):
        if animal_type == 'dog':
            return Dogs(name=name)
        elif animal_type == 'cat':
            return Cats(name=name)
        else:
            raise ValueError("Животное не существует")
