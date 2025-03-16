# Import the AfricanBigCat class from the animal_package
from animal_package.africanbigcat import AfricanBigCat
# Define a class named Lion that inherits from AfricanBigCat
class Lion(AfricanBigCat):
    def __init__(self, species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period, teeth_type, claw_retractable, roar_volume, mane_presence, pride_size, hunting_strategy, social_structure, territory_size, main_prey):
        # Initialize the Lion object with attributes, including those inherited from AfricanBigCat
        super().__init__(species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period, teeth_type, claw_retractable, roar_volume, mane_presence)
        self.pride_size = pride_size
        self.hunting_strategy = hunting_strategy
        self.social_structure = social_structure
        self.territory_size = territory_size
        self.main_prey = main_prey

    def display_lion_info(self):
        # Method to display information specific to Lions, along with inherited information
        super().display_africanbigcat_info()
        print(f"Pride Size: {self.pride_size}, Hunting Strategy: {self.hunting_strategy}, Social Structure: {self.social_structure}, Territory Size: {self.territory_size}, Main Prey: {self.main_prey}")

    def hunt(self):
        # Method to simulate the lion hunting
        print(f"The lion uses its {self.hunting_strategy} to hunt {self.main_prey}.")

    def roar(self):
        # Method to simulate the lion roaring
        print(f"The lion roars with a volume of {self.roar_volume}.")

    def establish_territory(self):
        # Method to simulate the lion establishing its territory
        print(f"The lion patrols its {self.territory_size} territory.")

    def socialize(self):
        # Method to simulate the lion socializing within its pride
        print(f"The lion interacts within its {self.social_structure} pride of {self.pride_size} members.")

    def rest(self):
        # Method to simulate the lion resting
        print("The lion rests in the shade.")