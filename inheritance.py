class Movie:
    def __init__(self, mood, character, theme, pacing, typical_elements, examples):
        self.mood = mood
        self.character = character
        self.theme = theme
        self.pacing = pacing
        self.typical_elements = typical_elements
        self.examples = examples

    def details(self):
        print(f"Movie Mood: {self.mood}, Character: {self.character}, Themes: {self.theme}, "
              f"Pacing: {self.pacing}, Typical Elements: {self.typical_elements}, Examples: {self.examples}")


class Action(Movie):
    def sound(self):
        print("Loud")


class Drama(Action):
    def speak(self):
        print("Adventure")


class SciFi(Drama):  # Renaming Sci_fi to SciFi (Python naming convention)
    def explain(self):
        print("Fast")


class Horror(SciFi):
    def scary(self):
        print("Pin the pants")


class Comedy(Horror):
    def giggle(self):
        print("It is awfully funny")

    def crackle(self):
        print("Kevin Hart")

    def dumb(self):
        print("It is stupid")

    def bore(self):
        print("It is a snooze fest")

    def moana(self):
        print("It is for kids")
drama = Drama("Emotional","Protagonist", "Love", "Slow","Tears","Titanic" )
drama.details()
drama.speak()
Sci_fi = SciFi("Futuristic","Aliens", "Technology", "Medium","Space","Starwars" )
Sci_fi.details()
Sci_fi.explain()
horror = Horror("Scary","Ghosts", "Fear", "Slow","Darkness","TheRing" )
horror.details()
horror.scary()
comedy = Comedy("Funny","Clowns", "Laughter", "Fast","Jokes","Hangover" )
comedy.details()
comedy.giggle()
comedy.crackle()  
comedy.dumb()
comedy.bore()
comedy.moana()
  