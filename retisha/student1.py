def student_details():
    print("---Welcome!---\nThis program is aimed at capturing student details and calculating the student's "
    "final mark over the different exams.\nPlease enter the student's details below.")
    

    student_num = int(input("\nHow many students do you want to capture and compute their final mark?: "))
    student_id = 1

    for i in range(student_num):  
        print(f"\n--- Student {student_id} ---")
        

        # Dictionary that captures the details.
        details = {
            'name': input("Enter student's name: "), 
            'age': int(input("Enter the student's age: ")), 
            'Gender': input("Enter student's gender: "),
            'Program': input("Enter student's program: "),
            'Course': input("Enter student's course: "),
            'Year_of_study': int(input("Enter student's year of study: ")),
            'Test_1_marks': float(input("Enter student's test 1 marks: ")), 
            'Test_2_marks': float(input("Enter student's test 2 marks: ")), 
            'Course_work_marks': float(input("Enter student's course work marks: ")),
            'Exam_mark': float(input("Enter student's exam mark: "))
            }

        # Identifying the two best done exams and putting them in a list.
        marks = [details["Test_1_marks"], details["Test_2_marks"], details["Course_work_marks"]]
        marks.sort(reverse=True)
        print(f"\nThe list of the marks arranged from the best done to the worst done: {marks}")

        # Getting the average of the two best done.
        average = (marks[1] + marks[2]) / 2
        print(f"The average of the best done is {average}")

        # Converting the average of the two best done to a mark that is out of 40.
        mark_of_40 = average * 0.4
        print(f"The mark out of 40 is {mark_of_40:.2f}")

        # Converting the exam mark to one that is out of 60.
        mark_of_60 = (details["Exam_mark"]) * 0.6
        print(f"The exam mark out of 60 is {mark_of_60:.2f}")

        # Calculating the final mark by adding the one out of 40 and the one out of 60.
        final_mark = mark_of_40 + mark_of_60
        print(f"\nThe student's final mark is {final_mark:.2f}")

        student_id += 1

student_details()