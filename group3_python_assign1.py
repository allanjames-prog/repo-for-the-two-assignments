
# define a function that will be used to capture data
def capture_student_details():
 
 #current a dictionary that will store student data
 student_details= {

  #while capturing the data  we use the input function to give the users the permission to enter data
  #the input function is the input function
 "Name:":input(" Enter student's Name:"),
 "Age:" : int(input("Enter student's Age:")),
 "Gender:" : input("Enter student's gender:"),
 "Program:": input("Enter student's Program:"),
 "Year of study:": int(input("Enter student's Year of study:")),
 "Faculty:" :input("Enter student's Faculty"),
 "Date of Birth:": input("Enter student's Date of birth(yy-mm-dd):"),
 }

 # calculate both the test1 ,test2 final mark and actual course work
 test1_marks = int(input("enter test1_marks"))
 test2_marks = int(input("enter test2_marks"))
 average =  (test1_marks + test2_marks)/2
 summation = average* 40/100
 final_exams = int(input("enter the final mark"))
 final_mark = (final_exams*60/100)
 actual_course_unit_mark =(summation+final_mark)

 # putting the student details into the dictionary
 student_details [ "actual_course_unit_mark"] = actual_course_unit_mark

#print the dictionary
 print("student_details")

 #to be able to print both the key and is value we use for
 for key,value in student_details.items():
  print(f"{key}:{value}")

  #and here we invoke the function
capture_student_details()
