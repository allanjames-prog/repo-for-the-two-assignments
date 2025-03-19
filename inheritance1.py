from inheritance import Action, Drama, SciFi, Horror, Comedy

# Creating instances and calling methods
action = Action("Exciting", "Villains", "Heroism", "Fast", "Explosions", "John Wick")
action.details()
action.sound()

drama = Drama("Emotional", "Protagonist", "Love", "Slow", "Tears", "Titanic")
drama.details()
drama.speak()

scifi = SciFi("Futuristic", "Aliens", "Technology", "Medium", "Space", "Star Wars")
scifi.details()
scifi.explain()

horror = Horror("Scary", "Ghosts", "Fear", "Slow", "Darkness", "The Ring")
horror.details()
horror.scary()

comedy = Comedy("Funny", "Clowns", "Laughter", "Fast", "Jokes", "Hangover")
comedy.details()
comedy.giggle()
comedy.crackle()
comedy.dumb()
comedy.bore()
comedy.moana()
