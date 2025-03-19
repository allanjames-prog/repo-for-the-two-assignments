#importing the class module from class2 module

from Edna1 import *

lion = Lion("mufasa", "mammals", "brown", "fedali", "roars", "small", "4")
lion.details()
lion.make_sound()

tiger = Tiger("shere khan", "mammals", "orange", "panthera", "growls", "large", "5")
tiger.details()
tiger.make_sound()

elephant = Elephant("dumbo", "mammals", "gray", "elephantidae", "trumpets", "huge", "10")
elephant.details()
elephant.make_sound()

dog = Dog("buddy", "canine", "golden", "retriever", "barks", "medium", "3")
dog.details()
dog.make_sound()

cat = Cat("whiskers", "feline", "white", "persian", "meows", "small", "2")
cat.details()
cat.make_sound()
cat.purr()
cat.scratch()
cat.sleep()
cat.eat()
cat.play()



"""import keyword
print(keyword.kwlist)"""
