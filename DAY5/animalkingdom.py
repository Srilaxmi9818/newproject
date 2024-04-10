class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} makes the sound: {self.sound}")

# Creating instances of Animal representing a dog and a cat
dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

# Calling make_sound on each instance
dog.make_sound()  # Output: Dog makes the sound: Woof
cat.make_sound()  # Output: Cat makes the sound: Meow
