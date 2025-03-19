def student_details():
      name = input("Enter students name: ")
      age = int(input("Enter students age: "))
      gender = input("Enter students gender: ")
      program = input("Enter students program: ")
      year_of_study = int(input("Enter students year of study: "))
      date_of_birth = input("Enter students date of birth: ")
      faculty = input("Enter students faculty: ")
      student_info ={"name":name,"age":age,"gender":gender,
                     "program":program,"year_of_study":year_of_study,
                     "date_of_birth":date_of_birth,"faculty":faculty,}
      return student_info
print(student_details())

def mark_sheet():
      test1 = int(input("Enter test1 marks: "))
      test2 = int(input("Enter test2 marks: "))
      final_exams = int(input("Enter final exams marks: "))
      print("sum_marks")
      sum_marks = test1 + test2
      print(sum_marks) 
      print("average_marks")
      average_marks = sum_marks / 2
      print(average_marks)
      final_tests_mark = average_marks * (40/100)
      print(f"marked ot of 40: {final_tests_mark}")
      final_exams_mark = final_exams / 100 * 60
      print(f"marked ot of 60: {final_exams_mark}")
      total_marks = final_tests_mark + final_exams_mark
      print(f"Total marks: {total_marks}")
      total_mark = round(total_marks, 1)
      return total_mark

print(mark_sheet())

"""using dynamic function together with input fuction
create student details name,age,gender,year of study,
program,test1 marks,test2 marks,course work marks and final exams.
calculate the two best done, the two best done is marked out of 40,
exam mark is marked out of 60"""

def student_details():
    
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    gender = input("Enter student gender: ")
    year_of_study = input("Enter year of study: ")
    program = input("Enter program: ")
    
    test1 = float(input("Enter Test 1 marks (out of 100): "))
    test2 = float(input("Enter Test 2 marks (out of 100): "))
    coursework = float(input("Enter Coursework marks (out of 100): "))
    final_exam = float(input("Enter Final Exam marks (out of 100): "))
    
    return student_details




      

        

       