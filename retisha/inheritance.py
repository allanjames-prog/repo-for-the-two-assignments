#creating a main class named bird with methods name, size, color,wingspan,order,habitat and feeding
class Bird:
    """Represents a bird with common attributes."""
    def __init__(self, name, size, color, wingspan, order, habitat, feeding):
        self.name = name
        self.size = size
        self.color = color
        self.wingspan = wingspan
        self.order = order
        self.habitat = habitat
        self.feeding = feeding

    def details(self):
#Prints detailed information about the bird.
        print(f"Name: {self.name}, Color: {self.color}, Size: {self.size}, Wingspan: {self.wingspan}, Order: {self.order}, Habitat: {self.habitat}, Feeding: {self.feeding}, Flight: {self.flight()}, Nesting: {self.nesting()}")
#Describes the bird's flight capabilities.
    def flight(self):
        return "Most birds can fly, using their wings to generate lift."
    
#Describes the bird's nesting behavior.
    def nesting(self):
        return "Birds build nests to lay eggs and raise their young."
    
#Represents an owl, inheriting from Bird."""
class Owl(Bird):
#Describes the owl's hunting behavior.
    def hunting(self):
        
        return "Owls are nocturnal hunters with excellent night vision."
#Represents an eagle, inheriting from Bird.""
class Eagle(Bird):
#Describes the eagle's vision.    
    def vision(self):
        return "Eagles have exceptional eyesight, allowing them to spot prey from great distances."
#Represents a hummingbird, inheriting from Bird
class Hummingbird(Bird):
#Describes the hummingbird's feeding behavior
    def feeding(self):
        return "Hummingbirds feed on nectar from flowers, using their long beaks and tongues."
#Represents a penguin, inheriting from Bird.
class Penguin(Bird):
#Overrides the flight method for penguins.    
    def flight(self):
        return "Penguins are flightless birds, using their wings for swimming instead."
#Describes the penguin's breeding behavior
    def breeding(self):
        return "Penguins breed in large colonies, often in harsh environments."

# Example usage
golden_eagle = Eagle("Golden Eagle", "large", "brown", "2 meters", "Falconiformes", "mountainous regions", "carnivore")
golden_eagle.details()

print(f"{golden_eagle.name}: {golden_eagle.vision()}")

# Create a hummingbird
ruby_throated_hummingbird = Hummingbird("Ruby-throated Hummingbird", "small", "green and red", "5 cm", "Apodiformes", "gardens and forests", "nectar")
print(ruby_throated_hummingbird.name)


