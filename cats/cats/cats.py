from random import choice


class Cats:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Vasya")
        self.sex = kwargs.get("sex", choice(['male', 'female']))
        self.color = kwargs.get("color", choice(['black', 'white', 'gray', 'red']))
        self.__hungry = 0

    def say(self):
        return "Meow!"

    def eat(self):
        self.hungry = self.hungry + 1
        return self.__hungry

    def pipi(self):
        self.hungry = self.hungry - 1
        return self.__hungry

    def set_hungry(self, num):
        if (isinstance(num, int)):
            self.__hungry = num
            return self.__hungry
        else:
            raise TypeError("Должно прийти число")

    def get_hungry(self):
        return self.__hungry

    def __str__(self):
        return f'Cats name {self.name}'


barsik = Cats(name="Barsik")
print(barsik.__dict__)
print(barsik.get_hungry())

barsik.set_hungry(-1)
print(barsik.get_hungry())

print(barsik)