import herit
#masavu = herit.Masavu("Nambaale_beans", "sweet", "5.1kcal", "plant-based", "Ug.shs 3500 per kg", "whitesmoke", "soft")    
#masavu.repair()


import student_details
def student_detail():
    print("WELCOME TO OUR STUDENTS' DETAILS FORM") 

    # List to store student details       
    students = []

    # Prompt user for the number of students    
    num_students = int(input("Please enter the number of students: "))

    # Loop to capture students' details    
    for i in range(num_students):
        print(f"\nPlease enter details for Student {i + 1}:")
        first_name = input("Enter student's first name:  ")
        last_name = input("Enter student's last name:  ")
        age = input("Enter student's age:  ")
        gender = input("Enter student's gender:  ")
        program = input("Enter student's program:  ")
        faculty = input("Enter student's faculty:  ")
        year_of_study = input("Enter year of study:  ")
        date_of_birth = input("Enter student's date of birth:  ")

        # Capture students' test scores and convert them to float
        test1_score = float(input("Enter test1 score: "))
        test2_score = float(input("Enter test2 score: "))
        coursework_score = float(input("Enter coursework score: "))
        exam_score = float(input("Enter exam score: "))

        # Obtain the average of the best two marks from test1, test2, and coursework
        best_two_marks = sorted([test1_score, test2_score, coursework_score], reverse=True)[:2]
        average_tests = sum(best_two_marks) / 2  

        # Obtain the final score with weights: 40% from tests and 60% from the exam
        final_score = (average_tests * 0.4) + (exam_score * 0.6)

        # Storing details in a dictionary        
        student = {
            "Student": f"Student {i + 1}",
            "First Name": first_name,
            "Last Name": last_name,
            "Age": age,
            "Gender": gender,
            "Program": program,
            "Faculty": faculty,
            "Year of Study": year_of_study,
            "Date of Birth": date_of_birth,
            "Test1 Score": test1_score,
            "Test2 Score": test2_score,
            "Coursework Score": coursework_score,
            "Exam Score": exam_score,
            "Final Score": final_score  
        }

        # Adding student detail to list
        students.append(student)

    # Sort students by final score in descending order
    students.sort(key=lambda x: x["Final Score"], reverse=True)

    # Displaying all students' details
    print("\nList of students (sorted by Final Score): ")

    for student in students:
        print(f"\n{student['Student']}:")  
        for key, value in student.items():
            if key != "Student":
                print(f"{key}: {value}")



from trees_flower_rainbow import turtle

mypen= turtle.Turtle()
mypen.shape('turtle')
mypen.speed(10)

window= turtle.Screen()
window.bgcolor('white')
rainbow= ['red','orange','yellow','green','blue','indigo','violet']
size= 180
mypen.penup()
mypen.goto(0,-180)
for color in rainbow:
	mypen.color(color)
	mypen.fillcolor(color)
	mypen.begin_fill()
	mypen.circle(size)
	mypen.end_fill()
	size-=20

turtle.done()



