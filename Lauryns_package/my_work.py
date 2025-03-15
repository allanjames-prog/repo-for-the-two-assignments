# creating a class of Reptiles
class Reptile:
    """creating the very first method that indicate the different attributes 
    that each object in the above mentioned class shoul have"""
    #creating an instructor that will be used to allocate objects in the class with their respective values
    def __init__(self, name,size,color,speed, order, habitat, feeding):
        self.name = name
        self.size = size
        self.color = color
        self.speed = speed
        self.order = order
        self.habitat = habitat
        self.feeding = feeding

    """details method displays all the attributes of an object in the class reptile 
     and also calls upon the reproduction and basking method"""
    def details(self):
        print(f"self.name: {self.name}, self.color: {self.color}, self.size: {self.size}, self.speed: {self.speed}, self.order: {self.order}, self.reproduction: {self.reproduction()}, self.basking: {self.basking} ")

    # this method in inherited by all objects under the class Reptiles
    def reproduction(self):
        # it indicates how reptiles reproduce
        return "This animal lays eggs"
    
    # this is a habit inherited by all objects under this particular class indicating how these animals regulet their body temperature
    def basking(sef):
        return "These animals spend time in sunlit areas to warm their bodies, " \
        "which helps with digestion and metabolic processes."

# Tortoise is a class that inherits from the main class Reptile meaning it takes on all the attributes possed by the main class to. 
class Tortoise(Reptile):
    # hibbernation metjod indicates an attribute that is specific to the class tortoise
    def hibbernation(sefl):
        return "They often bury themselves underground or seek shelter in a burrow to escape the cold."
    
# Turtle is a class that inherits from the Reptile meaning it takes on all the attributes possed by the main class to. 
class Turtle(Reptile):
    # breeding metjod indicates an attribute that is specific to the class tortoise
    def breeding(self):
        return "It majorly comes on land to lay its eggs" 
    
## The Crocodile class inherits from Reptile and has specific behaviors related to feeding.    
class Crocodile(Reptile):
    def feeding(self):
        return "This animal feeds on meat hence its a carnivorous animal"
    
# The Alligator class inherits from Reptile and has specific behaviors related to aggressiveness.
class Alligator(Crocodile):
    def aggressiveness(self):
        return "Generally more shy and less aggressive. They tend to avoid humans and retreat if threatened."

# The Snake class inherits from Reptile and has specific behaviors related to sound,sensing and molting.
class Snake(Reptile):
    def sound(self):
        return "This animal makes a hissing sound"
    
    def molting(self):
        return "snakes shed their skin regularly as they grow"

    def sensing():
        return "They use their tongue and heat-sensing pits for tracking prey."
    
# The Cobra class inherits from Snake which inherits from Reptile and has specific behaviors related to hooding.
class Cobra(Snake):
    def hood_formation(self):
        return "this animal can flare out the ribs around their necks to create a distinct hood when threatened."
    
# creating instances for object orinoco_crocodile under the class crocodile
orinoco_crocodile = Crocodile("Crocodile", "large", "green", "fast", "crocodylia", "stays on both land and water", "carnivore")
    
# creating instances for object galapagos_tortoise under thr class Tortoise
galapagos_tortoise = Tortoise("galapagos","small", "brown", "slow", "testudines", "stays on land", "herbivore")

# print the details of galápagos_tortoise inherited from the class Reptiles
galapagos_tortoise.details()

# printing the reproduction method for the tortoise object
print(f"{galapagos_tortoise.name} {galapagos_tortoise.reproduction()}")

# creating cobra instances
cobra = Cobra("Indian Cobra", "medium", "black", "fast", "squamata", "varied habitats", "carnivore")

# Print sound (hissing) for Cobra
print(f"{cobra.name}:{cobra.sound()}")


