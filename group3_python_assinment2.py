# define a function which will be used to capture student details
def capture_students_details():
    print("WELCOME TO THE STUDENT PERFORMANCE SYSTEM!")
    print("KINDLY, YOU WILL BE REQUIRED TO INPUT DATA WHERE NECESSARY. THANK YOU.")
    print("PLEASE INPUT THE STUDENT DETAILS")
    # create a list to store each student's data
    student_list = []
    data = int(input("Please enter the number of students: "))
    
    for _ in range(data):
        student_details = {
            "Name": input("Please enter student's Name: "),
            "Age": int(input("Please enter student's Age: ")),
            "Gender": input("Please enter student's Gender: "),
            "Program": input("Please enter student's Program: "),
            "Year of study": input("Please enter student's Year of study: "),
            "Test1": int(input("Please enter student's Test1: ")),
            "Test2": int(input("Please enter student's Test2: ")),
            "Course": int(input("Please enter student's Course: ")),
            "Final Mark": int(input("Please enter student's Final Mark: "))
        }
        print("WELCOME TO STUDENT DETAILS AND MARKS")
        # Accessing marks from the student's details
        marks = [student_details["Test1"], student_details["Test2"], student_details["Course"]]

        # Sorting the marks to get the top 2 marks
        best2_marks = sorted(marks, reverse=True)[:2]

        # Calculating the average score (40%)
        average_test = (sum(best2_marks) // 2) * 0.4

        # Getting the final exam mark (60%)
        final_mark = student_details["Final Mark"] * 0.6

        # Calculating the total marks out of 100%
        total_marks = average_test + final_mark

        # Adding the final marks to the student's dictionary
        student_details["Actual Mark"] = total_marks

        # Append the student's details to the student list
        student_list.append(student_details)

    return student_list



# Invoking the function and displaying each student's details
students = capture_students_details()
for student in students:
    for key, value in student.items():
        print(f"{key}: {value}")
    print("\n")  # Print a blank line between students' details