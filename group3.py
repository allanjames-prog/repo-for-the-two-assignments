 
#group 3 members ;1. Ahuriire Violah , 2.Sitati Patience, 3.Nakyigozi Syliva, 4. Laruyn Hope , 5.Lochap Faustine 6. Akello Cinderalla

def students_performance():
    # Welcoming remarks

    print("Welcome to the Student Performance System!")
    print("Kindly, you will be required to input data where necessary. Thank you.")

    # this is to create a space between the content below and that above
    print("\n")
    students_list = []
    num = int(input("Please enter the number of entries: "))  # Input for number of students

    # Loop to collect information for each student
    for _ in range(num):
        students = {}  # Initialize an empty dictionary for each student
        
        print("\n")
        # Collect student information
        students["name"] = input("Please enter student name: ")
        students["age"] = int(input("Please enter student age: "))
        students["gender"] = input("Please enter student gender (male or female): ")
        students["program"] = input("Please enter student's program: ")
        students["year_of_study"] = int(input("Please enter student's year of study: "))
        students["test1"] = int(input("Please enter marks scored in test1: "))
        students["test2"] = int(input("Please enter marks scored in test2: "))
        students["course_work"] = int(input("Please enter marks scored in course work: "))
        students["exam"] = int(input("Please enter marks scored in exam: "))

        # Calculate best_done and final_exam marks
        students["best_done"] = best_done(students["test2"],  students["test1"], students["course_work"])
        students["final_exam"] = final_exam(students["best_done"], students["exam"])

        # Append or add the student's data to the students_list
        students_list.append(students)

    return students_list

# Function to calculate the best done score (average of test2 and course work)
def best_done(test1, test2, course_work):
    # sort is the formula used to arrange data in either majorly ascending order meaning form smallest to largest
    # the reverse true means we are going to do the opposite of getting from largest to smallest
    # [:2] means we are getting the top 2 in the list  
    top_two = sorted([test1, test2, course_work], reverse=True)[:2]  # Get the best two scores
    return (sum(top_two) / 2) * 0.4 

# Function to calculate the final exam score based on the best done and exam marks
def final_exam(best_done, exam):
    return best_done + (exam * 0.6)

# Collect data for all students
all_students = students_performance()

# Print out the collected information for each student
for student in all_students:
 for key, value in student.items():
    print(f"{key}: {value}")
 print("\n") # Print a blank line between students' details

