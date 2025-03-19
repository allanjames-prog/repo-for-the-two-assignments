from animal_package.animal import Animal

# Define a class named Mammal that inherits from the Animal class
class Mammal(Animal):
    def __init__(self, species, habitat, lifespan, size, weight, diet, sound, fur_color, gestation_period):
         # Initialize the Mammal object with attributes, including those inherited from Animal
        super().__init__(species, habitat, lifespan, size, weight, diet, sound)
        self.fur_color = fur_color
        self.gestation_period = gestation_period

    def display_mammal_info(self):
        # Method to display information specific to Mammals, along with inherited information
        super().display_info()
        print(f"Fur Color: {self.fur_color}, Gestation Period: {self.gestation_period}")
