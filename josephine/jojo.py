class Food:
    def __init__(self,name,color,type,size):
        self.food = Food 
        self.name = name
        self.type = type
        self.color = color
        self.size =size
        


    def details(self):
         print(f"name:{self.name} type:{self.type} color:{self.color} size:{self.size}")

class Matooke (Food):
    def tasteless(self):
        print("matooke is tasteless")

class Plantain(Matooke):
    def sweet(self):
        print("plantain is sweet")


class Yellowbananas(Plantain):
    def sweet(self):
        print("yellowbananas are sweet")

class Mabungo(Yellowbananas):
    def sweeter(self):
        print("mabungo is sweeter")

matooke= Matooke("matoke" , "green", "mpologoma","medium")
matooke.details()
matooke.tasteless()

plantain = Plantain("plantian", "yellow","gonja", "small")
plantain.details()
plantain.sweet()

yellowbananas = Yellowbananas("yellowbananas", "yellow", "bogoya", "big")
yellowbananas.details()
yellowbananas.sweet()

mabungo =Mabungo("mabugo","bananas", "yellow", "bigger")
mabungo.details()
mabungo.sweet()

        
    
    