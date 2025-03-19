# Import classes and methods from the inherit file
"""import inherit
# Create an instance of Heirloom tomato and print its characteristics
heirloom_tomato = inherit.Heirloom("Heirloom", "Red", "Large", "Sweet and tangy", "Fleshy", "Thin", "Round")
heirloom_tomato.details()
heirloom_tomato.perishability()
heirloom_tomato.best_use()
heirloom_tomato.value()
heirloom_tomato.growth_type()
heirloom_tomato.water_content()
heirloom_tomato.seed_content()
#Print details of cherry tomato
cherry_tomato = inherit.Cherry("Cherry", "Red", "Small", "Sweet", "Firm", "Thin", "Round")
cherry_tomato.details()
cherry_tomato.perishability()
cherry_tomato.growth_type()

# print details of roma tomato
roma_tomato = inherit.Roma("Roma", "Red", "Medium", "Sweet", "Firm", "Thin", "Oval")
roma_tomato.details()
roma_tomato.perishability()
roma_tomato.water_content()

# print details of beefsteak tomato
beefsteak_tomato =inherit. Beefsteak("Beefsteak", "Red", "Very Large", "Sweet and juicy", "Fleshy", "Thin", "Round and flattened")
beefsteak_tomato.details()
beefsteak_tomato.perishability()
beefsteak_tomato.seed_content()

# print details of grape tomato
grape_tomato =inherit. Grape("Grape", "Red", "Tiny", "Sweet", "Firm", "Thin", "Oval")
grape_tomato.details()
grape_tomato.perishability()
grape_tomato.value()"""

# Import functions from students folder
import student
#Loop through sorted students and print their details
for student in student. students_data:

    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Gender: {student['gender']}")
    print(f"Year: {student['year']}")
    print(f"Test1: {student['test1']}")
    print(f"Test2: {student['test2']}")
    print(f"Coursework: {student['coursework']}")
    print(f"Exam: {student['exam']}")
    print(f"Best Mark: {student['best_mark']:.2f}")
    print(f"Final Mark: {student['final_mark']:.2f}")
    print("-" * 20)