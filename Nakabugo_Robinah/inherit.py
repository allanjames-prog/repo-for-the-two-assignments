  # Defining a base class for Fruit
class Fruit:
    def __init__(self, name, color, size, taste, texture, skinType, shape):
       # Creating class properties
        self.name = name
        self.color = color
        self.size = size
        self.taste = taste
        self.texture = texture
        self.skinType = skinType
        self.shape = shape

    # Method to print fruit details
    def details(self):
        print(f"Fruit name: {self.name}, Fruit color: {self.color}, Fruit size: {self.size}, Fruit taste: {self.taste}, Fruit texture: {self.texture}, Fruit skinType: {self.skinType}, Fruit shape: {self.shape}")

# Defining a subclass Tomato hat inherits from Fruit
class Tomato(Fruit):
    def perishability(self):
        print("Tomatoes are perishable")

# Defining subclasses for different types of tomatoes
# Each subclass inherits from tomato and adds unique characteristics
class Cherry(Tomato):
    def growth_type(self):
        print("Growth type is determinate")  

class Roma(Tomato):
    def water_content(self):
        print("High water content")

class Beefsteak(Tomato):
    def seed_content(self):
        print("It has many seeds")

class Grape(Tomato):
    def value(self):
        print("Rich in fiber")

class Heirloom(Tomato):
    def best_use(self):
        print("Best used for salads")
    
    def value(self):
        print("High in antioxidants")
    
    def growth_type(self):
        print("Growth type is indeterminate")
        
    def water_content(self):
        print("High water content")
    
    def seed_content(self):
        print("Has many seeds")

#Create an instance of Heirloom tomato and print its characteristics
heirloom_tomato = Heirloom("Heirloom", "Red", "Large", "Sweet and tangy", "Fleshy", "Thin", "Round")
heirloom_tomato.details()
heirloom_tomato.perishability()
heirloom_tomato.best_use()
heirloom_tomato.value()
heirloom_tomato.growth_type()
heirloom_tomato.water_content()
heirloom_tomato.seed_content()

# Print details of cherry tomato
cherry_tomato = Cherry("Cherry", "Red", "Small", "Sweet", "Firm", "Thin", "Round")
cherry_tomato.details()
cherry_tomato.perishability()
cherry_tomato.growth_type()

# Print details of Roma tomato
roma_tomato = Roma("Roma", "Red", "Medium", "Sweet", "Firm", "Thin", "Oval")
roma_tomato.details()
roma_tomato.perishability()
roma_tomato.water_content()

# Print details of beefsteak tomato
beefsteak_tomato = Beefsteak("Beefsteak", "Red", "Very Large", "Sweet and juicy", "Fleshy", "Thin", "Round and flattened")
beefsteak_tomato.details()
beefsteak_tomato.perishability()
beefsteak_tomato.seed_content()
# Print details of grape tomato
grape_tomato = Grape("Grape", "Red", "Tiny", "Sweet", "Firm", "Thin", "Oval")
grape_tomato.details()
grape_tomato.perishability()
grape_tomato.value()






        



