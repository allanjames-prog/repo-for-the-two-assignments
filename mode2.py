class Food:
    def __init__(self, name, type, color, aroma, size, texture, value, price):
        self.name = name
        self.type = type
        self.color = color
        self.aroma = aroma
        self.size = size
        self.texture = texture
        self.value = value
        self.price = price

#method to display the details of the food items
    def details(self):
        print(f"foodname: {self.name}\n"
              f"foodtype: {self.type}\n"
              f"foodcolor: {self.color}\n"
              f"foodaroma: {self.aroma}\n"
              f"foodsize: {self.size}\n"
              f"foodtexture: {self.texture}\n"
              f"foodvalue: {self.value}\n"
              f"foodprice: {self.price}") 
#fish class inherits from Food class
class Fish(Food):
    def shape(self):
        print("streamlined")

class Tilapia(Fish):
    def habit(self): 
        print("lives in fresh waters")

class Silverfish(Fish):
    def feeding(self):
        print("can spend months without eating")

class Nileperch(Fish):
    def weight(self):
        print("over 440 lbs")

class Catfish(Fish):
    def reproduction(self):
        print("mate and lay eggs while swimming")

    def shape(self):
        print("elongated eel like body") 

    def habit(self):
        print("lives in streams and ponds")

    def feeding(self):
        print("eats more as temperature increases")

    def weight(self):
        print("over 650 pounds")

tilapia_fish = Tilapia("Tilapia", "Fish", "Silver-Gray", "Mild", "Medium", "Scaly", "Nutritious", "$10")
#display details and specific behavour
tilapia_fish.details()
tilapia_fish.habit() 