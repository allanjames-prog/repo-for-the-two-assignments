print("Welcome to Group 4 calculator! Please fill in the details below ")
def capture_student_details():
    student = []
    num_students = int(input("What is the total number of all students?: "))
    for i in range(1, num_students +1):
        student_details = {
            "Name": input(f"Enter name for student{i}: " ),
            "Age": int(input(f"Enter student's Age: ")),
            "Gender": input(f"Enter student's Gender: "),
            "Course": input(f"Student's course: "),
            "Year": input(f"Year of study: "),
            "Test1": int(input(f"Test1 Marks: ")),
            "Test2": int(input(f"Test2 Marks: ")),
            "Course Work": int(input(f"Course Work Marks: ")),
            "Final": int(input(f"Final Exam Mark: "))
        }
        scores = [student_details["Test1"], student_details["Test2"], student_details["Course Work"]]
        best_two_scores = sorted(scores, reverse=True)[:2]
        average_score = sum(best_two_scores)/ 2

        final_mark = average_score * 0.4 + student_details['Final']* 0.6
        print("Total Marks") 
        print(final_mark)
        print("\n///////////////////////////////////////////////////////////////////")
    

        student.append(student_details)

    print("\nStudent Details:")
    for details in student:
        print(f"Name: {details['Name']}, Age: {details['Age']}, Gender: {details['Gender']}, Course: {details['Course']}, Test1: {details['Test1']}, Test2: {details['Test2']}, Course work: {details['Course Work']}, Final: {details['Final']}\n-------------------------------------------------------------")
    return student
print("\n......................................................................")
students_data = capture_student_details()
#print(students_data)
print("\n--------------------------------------------")

