'''
Use atleast 5 classes to demonstrate inheritance in python and use a constructor with atleast 7 parameters with 
corresponding properties and the last class should be taking on atleast 5 methods
'''
#This demonstration has 5 classes and 7 parameters with corressponding properties

class Vehicle:

    #This method has 7 parameters
    def __init__(self, brand, model, year, fuel_type, max_speed, seating_capacity, weight):

        #corresponding properties        
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.seating_capacity = seating_capacity
        self.weight = weight

    def details(self):
        print(f"Name: {self.brand}\nModel: {self.model}\nYear: {self.year}\nFuel Type: {self.fuel_type}")  

#inherits from Vehicle. It has two methods
class Car(Vehicle):
    def sound(self):
        print("It honks")

#arguments for object car
car = Car("Toyota", "Camry", 2022 , "Gasoline", 220, 5, 1500)
car.details()

#inherits from Car and Vehicle. It has three methods
class SportsCar(Car):
    def enginePower(self):
        print("Turbo speed")

#inherits from SportsCar, Car and Vehicle. It has four methods
class ElectricSportsCar(SportsCar):
    def batteryPowered(self):
        print("It charges with Electricity")

#inherits from ElectricSportsCar, SportsCar, Car and Vehicle. It has five methods
class AutonomusElectricSportsCar(ElectricSportsCar):
    def selfdrive(self):
        print("It works on self-drive")    


