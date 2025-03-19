class Human:
    def __init__(self, Name, Size, Color, Age, Gender, Immunity, Food, Height):
        self.name = Name
        self.size = Size 
        self.color = Color 
        self.age = Age 
        self.gender = Gender
        self.immunity = Immunity
        self._food = Food 
        self.height = Height

    def details(self):
        print(f"\nName: {self.name}, \nSize: {self.size} \nColor: {self.color} \nAge: {self.age} \nGender: {self.gender} \nImmunity: {self.immunity} \nFood: {self._food} \nHeight: {self.height}")

class Man(Human):
    def role(self):
        print("Role:Father")

class Occupation:
    def occupation():
        print("Occupation: Company CEO")

class Nationality:
    def nationality():
        print("Nationality:Ugandan")

class Residence:
    def residence():
        print("Residence:Muyenga")
 
man = Man("Alex Mukulu","Medium", "Brown", "35years", "Male", "Strong","All edibles", "Tall")
man.details()
man.role()




























"""class Woman(Human):
    def role(self):
        print("Role:Mother")

woman = Woman("Ashely", "Medium", "Chocolate brown", "30years", "Female", "Strong", "All edibles", "Medium")
woman.details()
woman.role()"""







