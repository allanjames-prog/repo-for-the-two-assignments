# parent class
class Food:
    def __init__(self, name, taste, calories, origin, price, color, texture):
        self.name = name
        self.taste = taste
        self.calories = calories
        self.origin = origin
        self.price = price
        self.color = color
        self.texture = texture

    def describe(self):
        print(f"I like {self.name} beans with {self.color} color, tasting {self.taste}, and contains {self.calories} kcal. it's Origin is : {self.origin}. with texture : {self.texture}. Price: Ug.shs{self.price}")    

# child classes 
class Protein(Food):
        def build(self):
             print(f"Builds and repairs body tissue, {self.origin}")  

class Legumes(Protein):
        def repair(self):
             print("they are nutritious")    

class Beans(Legumes):
     def get_energy(self):
          print(f"{self.name} is mostly available in our local grocery shops")

class Masavu(Beans):
     def eat(self):
          print(f"{self.name} is affordable in our homes")

     def low_calories(self):
             print(f"{self.name} beans have got low calories in them")    

     def expensive(self):
             print(f"{self.origin} are nutritious foods")  

     def immune_booster(self):
          print(f"{self.name} helps to boost our immune systems")         

     def get_fiber(self):
        print(f"{self.name} are high in fiber and considered as a superfood. it has got a {self.texture} texture. its Prices are relative: Ug.shs{self.price}")    

# creating an object
masavu = Masavu("Nambaale_beans", "sweet", "5.1kcal", "plant-based", "Ug.shs 3500 per kg", "whitesmoke", "soft")    

# calling the methods in all classes
masavu.describe()
masavu.build()
masavu.repair()
masavu.get_energy()     

# calling the methods in the 5th class
masavu.eat()
masavu.low_calories()
masavu.expensive()
masavu.immune_booster()
masavu.get_fiber()
