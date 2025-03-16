# Collects student details and calculates marks for each student.
def students_detail():
    # A welcoming message
    print("WELCOME TO STUDENTS RECORDS SYSTEM")
    # Initialize an empty list to store student dictionaries.
    students_list = []
    num = int(input("Please enter number of student entries: "))
    # Loop thtough a specified number of students
    for _ in range(num):
        student = {}
        student["name"] = input("Please enter student name: ")
        student["age"] = int(input("enter student age: "))
        student["gender"] = input("enter student gender (Male/Female): ")
        student["year"] = int(input("enter year of study: "))
        student["test1"] = int(input("enter test1 marks: "))
        student["test2"] = int(input("enter test2 marks: "))
        student["coursework"] = int(input("enter coursework marks: "))
        student["exam"] = int(input("enter exam mark: "))

        # Calculate best mark by selecting the two highest from test1, test2, coursework
        student["best_mark"] = calculate_best_mark(student["test1"], student["test2"], student["coursework"])

        # Calculate final mark
        student["final_mark"] = final_mark(student["best_mark"], student["exam"])

        students_list.append(student)
    return students_list

def calculate_best_mark(test1, test2, coursework):
    marks = [test1, test2, coursework]

     # Sort in descending order
    marks.sort(reverse=True) 
     # Select the two highest marks
    best_two = marks[:2] 
    return (sum(best_two) / 2) * 0.4

def final_mark(best_mark, exam):
    return best_mark + (exam * 0.6)

# Get students data
students_data = students_detail()

# Loop through sorted students and print their details
for student in students_data:
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

