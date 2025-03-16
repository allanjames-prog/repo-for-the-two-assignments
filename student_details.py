

# GROUP 5
def student_detail(students):
    print("WELCOME TO OUR STUDENTS' DETAILS FORM") 

# list to store student details       
    students = []

# prompt user for the number of students    
    num_students = int(input("Please enter the number of students: "))

# loop to capture students' details    
    for i in range(num_students):
        print(f"\n STUDENT {i + 1}:")
        first_name = input("enter student's first_name:  ")
        last_name = input("enter student's last_name:  ")
        age = input("enter student's age:  ")
        gender = input("enter student's gender:  ")
        program = input("enter student's program:  ")
        faculty = input("enter student's faculty:  ")
        year_of_study = input("enter year of study:  ")
        date_of_birth = input("enter student's date of birth:  ")


#capture students' test scores        
        test1_score = int(input("Enter test1 score: "))
        test2_score = int(input("Enter test2 score: "))
        coursework_score = int(input("Enter coursework score: "))
        exam_score = int(input("Enter exam score: ")) 
# obtain the average of the best two marks from test1, test2, and course work

        best_two_marks = sorted([test1_score, test2_score, coursework_score], reverse=True)[:2]
        average_tests = sum(best_two_marks)/2

# obtain the final score with weights: 40% from tests and 60% from the exam

        final_score = (average_tests * 0.4) + (exam_score * 0.6)

# storing details in a dictionary        

        student = {
            "Student": f"Student {i + 1}",  # Added student label
            "First_Name": first_name,
            "Last_Name": last_name,
            "Age": age,
            "Gender": gender,
            "Pogram": program,
            "Faculty": faculty,
            "Year_of_study": year_of_study,
            "Date_of_birth": date_of_birth,
            "Test1 Score": test1_score,
            "Test2 score": test2_score,
            "Coursework Score": coursework_score,
            "exam Score": exam_score,
            "Final Score": final_score
            
        }
# adding student detail to list
        students.append(student) 

# sort students by final score in descending order

        students.sort(key=lambda x: x["Final Score"], reverse = True)        

# displaying all students' details
        print("\n list of students(sorted by Final Score): ")

        for i, student in enumerate(students, start=1):
            print(f"\n student{i }:")     
            for key, value in student.items():
                print(f"{key}: {value}")
# calling the function to execute                
student_detail("students")
