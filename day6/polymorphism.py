class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

def describe_animal(animal):
    print(animal.make_sound())

# Example usage:
dog = Dog()
cat = Cat()

describe_animal(dog)  # Output: Woof
describe_animal(cat)  # Output: Meow
