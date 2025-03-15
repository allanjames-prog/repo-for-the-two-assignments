# pen.py
from inheritance1 import Cat, Wild_cat, Domestic, Stray, Germany, Kenyan_cat

# Create an instance of Cat
cat = Cat("Garry", 5, "Meows", "White", "Local", "Home")
cat.details()
cat.cheer()

# Create an instance of Wild_cat
wild = Wild_cat("Garry", 5, "Meows", "White", "Local", "Bush")
wild.details()
wild.example1()

# Create an instance of Domestic
domestic = Domestic("Happy", 3, "Meows", "Gray", "Half breed", "Home")
domestic.details()
domestic.curry()

# Create an instance of Stray
stray = Stray("Passion", 6, "Meows", "Speckled", "Exotic", "Zoo")
stray.details()
stray.barry()

# Create an instance of Germany
germany = Germany("Jarry", 2, "Meows", "Dark green", "Dual", "Home")
germany.details()
germany.behavior()

# Create another instance of Wild_cat to show more examples
wild2 = Wild_cat("Garry", 5, "Meows", "White", "Local", "Home")
wild2.details()
wild2.example1()
wild2.example2()
wild2.example3()
wild2.example4()
wild2.example5()
wild2.example6()
