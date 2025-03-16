 # Import the BigCat class from the animal_package
from animal_package.bigcat import BigCat
# Define a class named AfricanBigCat that inherits from BigCat
class AfricanBigCat(BigCat):
    def __init__(self, species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period, teeth_type, claw_retractable, roar_volume, mane_presence):
        # Define a class named AfricanBigCat that inherits from BigCat
        super().__init__(species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period, teeth_type, claw_retractable, roar_volume)
        self.mane_presence = mane_presence

    def display_africanbigcat_info(self):
        # Method to display information specific to AfricanBigCats, along with inherited information
        super().display_bigcat_info()
        print(f"Mane Presence: {self.mane_presence}")