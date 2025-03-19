class Animal:
    def __init__(Tina, name, breed, color, size, age):
        Tina.name = name
        Tina.breed = breed
        Tina.color = color
        Tina.size = size
        Tina.age = age

    def details(Tina):
        print(f"Animalname: {Tina.name}, Animalbreed: {Tina.breed}, Animalcolor: {Tina.color}, Animalage: {Tina.age}")

#here mammal inherits from class Animal   
class Mammal(Animal):
      def example(Tina):
           print("mammal") 

#hera class Carnivore inherits from mammal
class Carnivore(Mammal):
     def example2(Tina):
          print("Carnivore")

#here lion inherits from class carnivore
class Lion(Carnivore):
     def example3(Tina):
          print("Lion")
#here cub innherits from class lion
class Cub(Lion):
     def example4(Tina):
          print("Cub")
#here class pridemember inherits from class cub
class Pridemember(Cub):
     def example5(Tina):
          print("pridemember")

zebra = Mammal("zebra", "species", "white", "big", "old")
zebra.details()
zebra.example()

tiger = Carnivore("tiger","species", "yellow", "small", "young")
tiger.details()
tiger.example2()

congolion = Lion("congolion","species", "brown", "medium", "teenager")
congolion.details()
congolion.example3()


jaguarcub = Cub("jaguarcub","species", "grey", "big", "teenager")
jaguarcub.details()
jaguarcub.example4()

lioness = Pridemember("lioness","species", "goldencoat", "120-180kg", "16years")
lioness.details()
lioness.example5()










           




