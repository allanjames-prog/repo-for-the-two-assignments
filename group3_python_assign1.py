def capture_student_details():
 student_details= {
 "Name:":input(" Enter student's Name:"),
 "Age:" : int(input("Enter student's Age:")),
 "Gender:" : input("Enter student's gender:"),
 "Program:": input("Enter student's Program:"),
 "Year of study:": int(input("Enter student's Year of study:")),
 "Faculty:" :input("Enter student's Faculty"),
 "Date of Birth:": input("Enter student's Date of birth(yy-mm-dd):"),
 }
 test1_marks = int(input("enter test1_marks"))
 test2_marks = int(input("enter test2_marks"))
 average =  (test1_marks + test2_marks)/2
 summation = average* 40/100
 final_exams = int(input("enter the final mark"))
 final_mark = (final_exams*60/100)
 actual_course_unit_mark =(summation+final_mark)

 
 student_details [ "actual_course_unit_mark"] = actual_course_unit_mark


 print("student_details")
 for key,value in student_details.items():
  print(f"{key}:{value}")
capture_student_details()
