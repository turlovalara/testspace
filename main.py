class Cat():
    def __init__(self, breed, color, age):
        self._breed = breed
        self._color = color
        self._age = age

    def breed(self):
        return self._breed

    def color(self):
        return self._color

    def age(self):
        return self._age

    def age(self, new_age):
        if new_age > self._age:
            self._age = new_age
        return self._age


cat1 = Cat('Сфинкс', 'черный', 5)
cat2 = Cat('Герман-рекс', 'черепаховый', 2)

print(cat1.breed)
print(cat2._color)
print(cat1.age)


class HomeCat(Cat):
    def __init__(self, breed, color, age, master, name):
        super().__init__(breed, color, age)
        self._master = master
        self._name = name

    def master(self):
        return self._master

    def name(self):
        return self._name

cat3 = HomeCat('Сфинкс', 'розовый', 5, 'Лариса', 'Семён')

print(cat3.master)
print(cat3._name)