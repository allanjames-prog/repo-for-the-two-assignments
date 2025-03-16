class Animal:
    def __init__(self, name, breed, color, family, sound, size, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.family = family
        self.sound = sound
        self.size = size
        self.age = age

    def details(self):
        print(f"animalname: {self.name} animalbreed: {self.breed} animalcolor:{self.color} animalfamily: {self.family} animalsound: {self.sound} animalsize {self.size} animalage: {self.age}")

class Lion(Animal):
    def make_sound(self):
        print("I Roar")

class Tiger(Animal):
    def make_sound(self):
        print("I Growl")

class Elephant(Animal):
    def make_sound(self):
        print("I Trumpet")

class Dog(Animal):
    def make_sound(self):
        print("I Bark")

class Cat(Animal):
    def make_sound(self):
        print("I Meow")

    def purr(self):
        print("I Purr")

    def scratch(self):
        print("I Scratch")

    def sleep(self):
        print("I Sleep")

    def eat(self):
        print("I Eat")

    def play(self):
        print("I Play")
"""""
lion = Lion("mufasa", "mammals", "brown", "fedali", "roars", "small", "4")
lion.details()
lion.make_sound()

tiger = Tiger("shere khan", "mammals", "orange", "panthera", "growls", "large", "5")
tiger.details()
tiger.make_sound()

elephant = Elephant("dumbo", "mammals", "gray", "elephantidae", "trumpets", "huge", "10")
elephant.details()
elephant.make_sound()

dog = Dog("buddy", "canine", "golden", "retriever", "barks", "medium", "3")
dog.details()
dog.make_sound()

cat = Cat("whiskers", "feline", "white", "persian", "meows", "small", "2")
cat.details()
cat.make_sound()
cat.purr()
cat.scratch()
cat.sleep()
cat.eat()
cat.play()"""
