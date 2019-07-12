class Animal:
    """Base class for Animals.

    Instance variables:
    - name: str
    - age: int
    - position: 0


    """
    hair = None
    scales = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.position = 0

    def move_up(self):
        self.position += 1
        print(f'{self.name} moved from {self.position -1} to {self.position}')

    def move_down(self):
        self.position -= 1
        print(f'{self.name} moved from {self.position + 1} to {self.position}')


class Mammal(Animal):

    hair = True

    def speak(self):
        pass


class Reptile(Animal):

    scales = True


class Human(Mammal):

    species = 'Homosapien'

    def speak(self):
        print(f'My name is {self.name}, I am {self.age} years old')


class Doggo(Mammal):

    species = 'Canine'

    def speak(self):
        return f'{self.name} says "Woof"'


class Iguana(Reptile):

    species = 'Lizard'

    def hiss(self):
        return f'{self.name} says "Hiss"'
