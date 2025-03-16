from animal_package.lion import Lion

#Create an instance of the Lion class with specific attributes.
lion = Lion(
    species="Lion",
    habitat="Savannah",
    lifespan="10-14 years",
    size="Large",
    weight="150-250 kg",
    diet="Carnivore",
    sound="Roar",
    fur_color="Golden",
    gestation_period="110 days",
    teeth_type="Sharp canines",
    claw_retractable=True,
    roar_volume="114 decibels",
    mane_presence=True,
    pride_size="15",
    hunting_strategy="Cooperative hunting",
    social_structure="Hierarchical",
    territory_size="100 sq km",
    main_prey="Zebras, Wildebeest"
)
# Call methods on the lion object to display information and simulate behavior.
lion.display_lion_info()
lion.make_sound()
lion.hunt()
lion.roar()
lion.establish_territory()
lion.socialize()
lion.rest()