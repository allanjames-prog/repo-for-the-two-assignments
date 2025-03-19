#Welcome message
print("Welcome to the Student Management System!")
print("Please enter the student's details as prompted below.\n")
def student_details():
    # Store details of multiple students
    student_list = []  

      # Loop for two students
    for i in range(2): 
        print(f"--- Student {i + 3} ---")

        # A dictionary to store student's details
        student = {
            "name": input("Please enter your name: "),
            "age": input("Enter your age: "),
            "gender": input("Enter your gender: "),
            "program": input("Enter your program: "),
            "year_of_study": input("Enter your year of study: "),
            "test1": int(input("Enter your test 1 score: ")),
            "test2": int(input("Enter your test 2 score: ")),
            "coursework": int(input("Enter your coursework score: ")),
            "final_exam": int(input("Enter your final exam score: ")),
        }

        # Accessing our marks from the dictionary, student
        marks = [student["test1"], student["test2"], student["coursework"]]

        # Sorting our marks to get the two top marks in descending order
        best_two_marks = sorted(marks, reverse=True)[:2]

        # Calculating our average score for out of 40%
        average_tests = (sum(best_two_marks) / 2) * 0.4

        # Calculating our final mark out of 60%
        final_exam_mark = student["final_exam"] * 0.6

        # Calculating our total marks out of 100%
        total_marks = average_tests + final_exam_mark

        # Adding the final marks to our dictionary
        student.update({"actual_mark": total_marks})
        student_list.append(student) #append the student dictionary to the list

    return student_list #return the list of students

# Invoking our function
student_data = student_details()

# Print the details of each student
for student in student_data:
    print("\nStudent Details:")
    for key, value in student.items():
        print(f"{key}: {value}")
        
        ''''
        MEMBERS;
        Agenorwot patience
        Maltida Sandra Akello
        Hellen
        Arthur
        Omar Ali
        Hienok
        Emma
        '''