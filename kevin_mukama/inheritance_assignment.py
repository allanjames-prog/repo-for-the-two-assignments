"""
Use atleast five classes to demostrate inheritance in python. 
Use a constructor with atleast seven  parameters and corresponding properties.
The last class of the inheritance chain should be taking on atleast five methods.

"""
#A child class can access methods from its parent class, 
# but a parent class cannot access methods from its child class

class World:
    def __init__(self, country, nationality, currency, food, climate, language, export):
        self.country = country
        self.nationality = nationality
        self.currency = currency
        self.food = food
        self.climate = climate
        self.language = language
        self.export = export

class Africa(World):
    def fav_sport(self):
        print("football")

class Uganda(Africa):
    def street_food(self):
        print("nyanya mbisi")

class Kampala(Uganda):
     def __init__(self, country, nationality, currency, food, climate, language, export, imports):
        super().__init__(country, nationality, currency, food, climate, language, export)
        self.imports = imports

class Makindye(Kampala):
    def region(self):
        print("central")

    def position(self):
        print("south")

    def population(self):
        print("1m")

    def games(self):
        print("all kinds")

    def method_5(self):
        print("still thinking")

kevin = Makindye("Uganda", "Ugandan", "Ugx", "matooke", "mild", "English", "coffee", "oil")
print(kevin.imports) #not kevin.imports() because imports is not a method yet you are calling it.
kevin.street_food()
kevin.method_5()
print(kevin.language)