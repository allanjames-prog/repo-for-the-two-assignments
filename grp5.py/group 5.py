def capture_students():
 """ 
Function to capture student details, calculate their final scores,
and display the information in a sorted manner.
 """
print("YOUR WARMLY WELCOME TO OUR FILL FORM.")
# List to store student details
students = []

# Prompt user for the number of students
num_students = int(input("Could you please enter the number of students: "))

# Loop to gather each student's details
for i in range(num_students):
        print(f"\nPlease enter details for Student {i + 1}:")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        gender = input("Enter student gender: ")
        program = input(" Enter program of study: ")
        year_of_study = input("please enter the year of study: ")
        faculty = input("Please enter the  faculty: ")

# Input for the test scores
        test1_score = int(input("Please  enter Test 1 score: "))
        test2_score = int(input(" Enter Test 2 score: "))
        coursework_score = int(input("Enter Coursework score: "))
        exam_score = int(input("Enter Exam score: "))

# Calculate the average of the best two marks out of test1, test2, and coursework
        best_two_scores = sorted([test1_score, test2_score, coursework_score], reverse=True)[:2]
        average_tests = sum(best_two_scores) / 2

# Calculate the final score with weights: 40% from tests and 60% from the exam
        final_score = (average_tests * 0.4) + (exam_score * 0.6)

# Storing details in a dictionary
        student = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Program": program,
            "Year of Study": year_of_study,
            "Faculty": faculty,
            "Test1 Score": test1_score,
            "Test2 Score": test2_score,
            "Coursework Score": coursework_score,
            "Exam Score": exam_score,
            "Final Score": final_score
        }
        
# Adding student details to the list
        students.append(student)

# Sort students by final score in descending order
students.sort(key=lambda x: x["Final Score"], reverse=True)

# Displaying all student details
print("\nList of Students (sorted by Final Score):")
for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}:")
        for key, value in student.items():
            print(f"{key}: {value}")
            #print(student)

# Calling the function to execute
capture_students()

