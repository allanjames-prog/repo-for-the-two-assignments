class Animal:
    def __init__(self, species, habitat, lifespan, size, weight, diet, sound):
        # Constructor for the Animal class, initializes basic animal attributes.
        self.species = species
        self.habitat = habitat
        self.lifespan = lifespan
        self.size = size
        self.weight = weight
        self.diet = diet
        self.sound = sound

    def make_sound(self):
        # Method to simulate the animal making its characteristic sound.
        print(f"The {self.species} makes a {self.sound} sound.")

    def display_info(self):
        # Method to display the basic information about the animal.
        print(f"Species: {self.species}, Habitat: {self.habitat}, Lifespan: {self.lifespan}, Size: {self.size}, Weight: {self.weight}, Diet: {self.diet}")

