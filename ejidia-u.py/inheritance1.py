class Animal:
    def __init__( self, name, age , sound ,color, breed, habitat):
       self.name = name
       self.age = age
       self.sound = sound
       self.color = color 
       self.breed = breed
       self.habitat = habitat
      
    def details(self):
           print(f" name:  {self.name}\n age :  {self.age}\n sound:  {self.sound} \n color:  {self.color}\n breed:  {self.breed} \n habitat:  {self.habitat}")

class Cat(Animal):
    def cheer(self):
        print("Meows")

class Domestic(Cat):
    def curry(cat):
        print("Black")

class Stray(Domestic):
    def barry(local):
        print( "Max")

class Germany(Stray):
    def behavior(big):
        print("Huge")

class Kenyan_cat(Germany):
    def color(Bingo):
        print("Bingo")

class Wild_cat( Kenyan_cat):
    def example1(self):
        print("Example 1 is a bush cat")

    def example2(self):
        print("Example 2 is a berry cat")
    
    def example3(self):
        print("Example3 is a domestic cat")

    def example4(self):
        print( "Example4 is a wild cat")

    def example5(self):
        print("Example 4 is a sweet cat")

    def example6(self):
        print("Example6 is a  bitter cat" )


cat = Cat("Garry", 5 ,"Meows", "White", "Local", "Home")
cat.details()
cat.cheer()
 
wild = Wild_cat("Garry", 5 ,"Meows", "White", "Local", "Bush")
wild.details()
wild.example1()

domestic =Domestic ("Happy", 3 ,"Meows", "Gray", "Half breed", "Home")
domestic.details()
domestic. curry()

stray = Stray("passion", 6 ,"Meows", "Speckled", "Exotic", "Zoo")
stray.details()
stray.barry()

germany = Germany("Jarry", 2 ,"Meows", "Dark green", "Dual", "Home")
germany.details()
germany.behavior()

wild = Wild_cat("Garry", 5 ,"Meows", "White", "Local", "Home")
wild.details()
wild.example1()
wild.example2()
wild.example3()
wild.example4()
wild.example5()
wild.example6()


        





     





























































































































