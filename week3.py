class Animal:
    def __init__(self, name, color, size):
        # Initializing attributes for the Animal class
        self.name = name
        self.color = color
        self.size = size
    def details(self):
         # Method to print details of the animal
        print(f"animalname: {self.name} animalcolor: {self.color}")


class Dog(Animal):
    def sound(self):
         # Method specific to Dog class
        print("dog woooofs")
# Creating an instance of Dog

dog = Dog("Scorbi", "black", "big")
dog.details()
dog.sound()
        


class Bulldog(Dog):
     # method for bulldog class
    def greet(self):
        print("it wigs")
bulldog = Bulldog("smart", "brown", "large")
bulldog.details()
bulldog.sound()
bulldog.greet()


class Cat(Bulldog):
    def play(self):
         # Method specific to Cat class
        print("it jumps")
cat = Cat("slender", "black", "small")
cat.details()# Displaying details of Cat
cat.sound()    # Cat makes sound (inherited from Dog)
cat.greet()    # Cat greets (inherited from Bulldog)
cat.play()     # Cat plays (own method)


