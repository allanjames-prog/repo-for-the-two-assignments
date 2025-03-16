# Import the Carnivore class from the animal_package
from animal_package.carnivore import Carnivore

# Define a class named Feline that inherits from Carnivore
class Feline(Carnivore):
    def __init__(self, species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period, teeth_type, claw_retractable):
        # Initialize the Feline object with attributes, including those inherited from Carnivore
        super().__init__(species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period, teeth_type)
        self.claw_retractable = claw_retractable

    def display_feline_info(self):
        # Method to display information specific to Felines, along with inherited information
        super().display_carnivore_info()
        print(f"Claws Retractable: {self.claw_retractable}")