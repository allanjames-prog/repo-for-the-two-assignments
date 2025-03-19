# Import the Mammal class from the animal_package
from animal_package.mammal import Mammal
# Define a class named Carnivore that inherits from Mammal
class Carnivore(Mammal):
    def __init__(self, species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period, teeth_type):
        # Initialize the Carnivore object with attributes, including those inherited from Mammal
        super().__init__(species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period)
        self.teeth_type = teeth_type

    def display_carnivore_info(self):
        # Method to display information specific to Carnivores, along with inherited information
        super().display_mammal_info()
        print(f"Teeth Type: {self.teeth_type}")