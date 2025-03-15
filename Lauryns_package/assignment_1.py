#a fn capturing student details
def capture_details(student):
    #create a dictionary called student
    student = {
        "name":input("enter name of the student"),
        "age":int(input("enter age of the student")),
        "gender":input("enter gender of the student"),
        "program":input("enter program of the student"),
        "year of study":int(input("enter year of study of the student")),
        "test1":int(input("enter test1 marks of the student")),
        "test2":int(input("enter test2 marks of the student")),
        "course_work":int(input("enter course work marks of the student")),
        "exam":int(input("enter exam marks of the student")),
    }
#accessing marks from the dictionary
    marks = [student["test1"], student["test2"], student["course_work"]]

    #sorting best done 
    best_two = sorted(marks, reverse = True)[:2]

    #calculating the average
    average_test = (sum(best_two)/2) * 0.4
    
    #calculating the exam mark
    exam = student["exam"] * 0.6

    #calculating the final exam marks
    final_exam_marks = average_test + exam

    #adding the final actual mark to the dictionary
    student.update({"actual_mark":final_exam_marks})
    return student
for key, value in capture_details("student").items():

  print(f"{key} : {value}\n")
print(capture_details("student"))