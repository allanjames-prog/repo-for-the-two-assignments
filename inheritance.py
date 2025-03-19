<<<<<<< HEAD
class Movie:
    def __init__(self, mood, character, theme, pacing, typical_elements, examples):
        self.mood = mood
        self.character = character
        self.theme = theme
        self.pacing = pacing
        self.typical_elements = typical_elements
        self.examples = examples

    def details(self):
        print(f"Movie Mood: {self.mood}, Character: {self.character}, Themes: {self.theme}, "
              f"Pacing: {self.pacing}, Typical Elements: {self.typical_elements}, Examples: {self.examples}")


class Action(Movie):
    def sound(self):
        print("Loud")


class Drama(Action):
    def speak(self):
        print("Adventure")


class SciFi(Drama):  # Renaming Sci_fi to SciFi (Python naming convention)
    def explain(self):
        print("Fast")


class Horror(SciFi):
    def scary(self):
        print("Pin the pants")


class Comedy(Horror):
    def giggle(self):
        print("It is awfully funny")

    def crackle(self):
        print("Kevin Hart")

    def dumb(self):
        print("It is stupid")

    def bore(self):
        print("It is a snooze fest")

    def moana(self):
        print("It is for kids")
drama = Drama("Emotional","Protagonist", "Love", "Slow","Tears","Titanic" )
drama.details()
drama.speak()
Sci_fi = SciFi("Futuristic","Aliens", "Technology", "Medium","Space","Starwars" )
Sci_fi.details()
Sci_fi.explain()
horror = Horror("Scary","Ghosts", "Fear", "Slow","Darkness","TheRing" )
horror.details()
horror.scary()
comedy = Comedy("Funny","Clowns", "Laughter", "Fast","Jokes","Hangover" )
comedy.details()
comedy.giggle()
comedy.crackle()  
comedy.dumb()
comedy.bore()
comedy.moana()
  
=======
class Animal:
    def __init__(animal,name,species,age, weight,habitat,diet,sound):
        animal.name = name
        animal.species = species
        animal.age = age
        animal.weight= weight
        animal.habitat =habitat
        animal.diet = diet
        animal.sound = sound

    def make_sound(animal):
        return f"{animal.name} says {animal.sound}!"
    def display_info(animal):
        return (f"Name: {animal.name}, Species: {animal.species}, Age: {animal.age}, "
                f"Weight: {animal.weight}kg, Habitat: {animal.habitat}, Diet: {animal.diet}")

# Derived class 1
class Mammal(Animal):
    def __init__(animal, name, species, age, weight, habitat, diet, sound, is_domestic, fur_type):
        super().__init__(name, species, age, weight, habitat, diet, sound)
        animal.is_domestic = is_domestic
        animal.fur_type = fur_type

    def display_mammal_info(animal):
        return f"{animal.display_info()}, Domestic: {animal.is_domestic}, Fur Type: {animal.fur_type}"

# Derived class 2
class Bird(Animal):
    def __init__(animal, name, species, age, weight, habitat, diet, sound, wingspan, can_fly):
        super().__init__(name, species, age, weight, habitat, diet, sound)
        animal.wingspan = wingspan
        animal.can_fly = can_fly

    def display_bird_info(animal):
        return f"{animal.display_info()}, Wingspan: {animal.wingspan}m, Can Fly: {animal.can_fly}"

# Derived class 3
class Fish(Animal):
    def __init__(animal, name, species, age, weight, habitat, diet, sound, water_type, fin_count):
        super().__init__(name, species, age, weight, habitat, diet, sound)
        animal.water_type = water_type
        animal.fin_count = fin_count

    def display_fish_info(animal):
        return f"{animal.display_info()}, Water Type: {animal.water_type}, Fin Count: {animal.fin_count}"

# Derived class 4
class Reptile(Animal):
    def __init__(animal, name, species, age, weight, habitat, diet, sound, is_venomous, scale_type):
        super().__init__(name, species, age, weight, habitat, diet, sound)
        animal.is_venomous = is_venomous
        animal.scale_type = scale_type

    def display_reptile_info(animal):
        return f"{animal.display_info()}, Venomous: {animal.is_venomous}, Scale Type: {animal.scale_type}"

# Derived class 5 with five methods
class Amphibian(Animal):
    def __init__(animal, name, species, age, weight, habitat, diet, sound, is_aquatic, skin_type):
        super().__init__(name, species, age, weight, habitat, diet, sound)
        animal.is_aquatic = is_aquatic
        animal.skin_type = skin_type

    def display_amphibian_info(animal):
        return f"{animal.display_info()}, Aquatic: {animal.is_aquatic}, Skin Type: {animal.skin_type}"

    def swim(animal):
        return f"{animal.name} is swimming in the water."

    def jump(animal):
        return f"{animal.name} is jumping on land."

    def croak(animal):
        return f"{animal.name} is croaking loudly: {animal.sound}!"

    def shed_skin(animal):
        return f"{animal.name} is shedding its {animal.skin_type} skin."

    def hibernate(animal):
        return f"{animal.name} is hibernating during the winter."

"""frog = Amphibian("Froggie", "Frog", 2, 0.5, "Pond", "Insects", "Ribbit", True, "Smooth")
print(frog.display_amphibian_info())
print(frog.swim())
print(frog.jump())
print(frog.croak())
print(frog.shed_skin())
print(frog.hibernate())"""
      

    
>>>>>>> 47d9117d1ccf5fc8ef71a86bd9f8718d0cc7285c
