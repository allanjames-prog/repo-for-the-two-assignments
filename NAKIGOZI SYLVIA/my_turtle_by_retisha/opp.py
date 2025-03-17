
class Dog:
    def __init__(self,name,):
        self.name = name 
    
        print(name)

        pass

    def add_ones(self, x):
        return x+1
    def bark(self):
        print("bark")
    def get_name(self):
        return self.name
animal = Dog("JESY")

    
print(animal.name)
animal2 = Dog('Max')
print(animal2.get_name())
animal.bark()
print(animal.add_ones(8))
print(type(animal))
