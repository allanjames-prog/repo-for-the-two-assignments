# Import the Feline class from the animal_package
from animal_package.feline import Feline
# Define a class named BigCat that inherits from Feline
class BigCat(Feline):
    def __init__(self, species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period, teeth_type, claw_retractable, roar_volume):
        # Initialize the BigCat object with attributes, including those inherited from Feline
        super().__init__(species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period, teeth_type, claw_retractable)
        self.roar_volume = roar_volume

    def display_bigcat_info(self):
        # Method to display information specific to BigCats, along with inherited information
        super().display_feline_info()
        print(f"Roar Volume: {self.roar_volume}")