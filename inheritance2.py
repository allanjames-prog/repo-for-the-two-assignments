#importing the inheritance module to inheritance2 module
from inheritance import*


frog = Amphibian("Froggie", "Frog", 2, 0.5, "Pond", "Insects", "Ribbit", True, "Smooth")
print(frog.display_amphibian_info())
print(frog.swim())
print(frog.jump())
print(frog.croak())
print(frog.shed_skin())
print(frog.hibernate())