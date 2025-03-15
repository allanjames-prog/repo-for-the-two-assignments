class Animal:
    def __init__(self, name, type, color, size, sound, price, age):
        # Initialize the Animal object with basic attributes.
        # We're storing information like name, what kind of animal it is, etc.
        self.name = name 
        self.type = type  
        self.color = color  
        self.size = size  
        self.sound = sound
        self.price = price  
        self.age = age  

    def details(self):
        # This is like showing all the information we stored about the animal.
        print(f"animalname: {self.name}\n"
              f"animaltype: {self.type}\n"
              f"animalcolor: {self.color}\n"
              f"animalsize: {self.size}\n"
              f"animalsound: {self.sound}\n"
              f"animalprice: {self.price}\n"
              f"animalage: {self.age}")

class Cow(Animal):
    def shape(self):
        # This is something special only cows have, a shape description.
        print("royalty-f")

class DairyPesa(Cow):
    def habit(self):
        # A special thing DairyPesa cows do.(chewing the cud)
        print("ruminating")  

class HolsteinFriesian(Cow):
    def feeding(self):
        # What Holstein Friesian cows like to eat.
        print("grasses")

class Hereford(Cow):
    def weight(self):
        # How heavy Hereford cows are.
        print("over 900 kg")

class Simmental(Cow):
    def reproduction(self):
        # How Simmental cows have babies.
        print("calving interval")

class Jersey(Cow):
    def color(self):
        # One color of Jersey cows.
        print("black")

    def shape(self):
        # Another shape feature of Jersey cows.
        print("broad face with long eyelashes")

    def habit(self):
        # A habit of Jersey cows.
        print("resting")

    def feeding(self):
        # What Jersey cows eat.
        print("grains and supplements")

    def weight(self):
        # How heavy Jersey cows are.
        print("over 800 kgs")

    def reproduction(self):
        # How Jersey cows reproduce.
        print("ovary produces the egg")

    def color(self):
        # More colors of Jersey cows.
        print("black, white, brown")

animal1 = Animal("Generic Animal", "Mammal", "Various", "Medium", "Various", 100, 5)
cow1 = Cow("Generic Cow", "Mammal", "Brown", "Large", "Moo", 1000, 3)
dairy_pesa1 = DairyPesa("DairyPesa 1", "Mammal", "Black and White", "Large", "Moo", 1200, 4)
holstein_friesian1 = HolsteinFriesian("Holstein Friesian 1", "Mammal", "Black and White", "Large", "Moo", 1500, 5)
hereford1 = Hereford("Hereford 1", "Mammal", "Red and White", "Large", "Moo", 1800, 6)
simmental1 = Simmental("Simmental 1", "Mammal", "Red and White", "Large", "Moo", 2000, 7)
jersey1 = Jersey("Jersey 1", "Mammal", "Brown", "Medium", "Moo", 2500, 8)

print("Animal Details:")
animal1.details()
print("\nCow Details:")
cow1.details()
cow1.shape()
print("\nDairyPesa Details:")
dairy_pesa1.details()
dairy_pesa1.shape()
dairy_pesa1.habit()
print("\nHolstein Friesian Details:")
holstein_friesian1.details()
holstein_friesian1.shape()
holstein_friesian1.feeding()
print("\nHereford Details:")
hereford1.details()
hereford1.shape()
hereford1.weight()
print("\nSimmental Details:")
simmental1.details()
simmental1.shape()
simmental1.reproduction()
print("\nJersey Details:")
jersey1.details()
jersey1.shape()
jersey1.habit()
jersey1.feeding()
jersey1.weight()
jersey1.reproduction()





