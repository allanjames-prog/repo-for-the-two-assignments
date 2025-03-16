def student_details():
    details = {"name": input("Student_name"), 
               "gender": input("enter gender"),
               "date of birth":input("date of birth"), 
               "age": int(input("Enter age")),
               "program": input("Enter program"),
               "year of study": int(input("Enter year of study")),
               "faculty": input("Enter the faculty"),
               "test1_marks": int(input("Enter test1 marks")),
               "test2_marks": int(input("Enter test2 marks")),
               "final_marks": int(input("Enter final marks")), }
    
    sum = (((details["test1_marks"]) + (details["test2_marks"]))/2)*0.4
    final_mark = details["final_marks"]*0.6
    total = sum + final_mark
    print(f"average out of 40 is {sum}")
    print(f"final_marks is {final_mark}")
    print(f"total is {total}")
student_details()

#dynamic functions where values are expected at the call
def add():#stactic have fixed values in their valuabes
    a = 5
    b = 10
    return a + b
print(add())

def add1(a, b): #dynamic expect values at the call of the function
    return a + b
#a variable within braces of a function are called parameters
print(add1(20, 50))
print(add1(49, 70))
print(add1(65, 15))

#Another example of dynamic functions
def student_details(name, age, gender, course, year_of_study, test1_marks, test2_marks, course_work_marks,exam_mark):
    student_info = {
        "name": name,
        "age": age,
        "gender": gender,
        "course": course,
        "year_of_study": year_of_study,
        "test1_marks": test1_marks,
        "test2_marks": test2_marks,
        "course_work_marks": course_work_marks,
        "exam_mark": exam_mark
    }
    return student_info

student1 = student_details("Athens", 12, "female", "computing", 2024, 83, 80, 85, 90,)
student2 = student_details("Philmon", 12, "male", "computing", 2024, 75, 85, 90, 92)

print(student1)
print(student2)
def calculate_final_marks(name, test1_marks, test2_marks, course_work_marks, exam_mark):
    best_test_mark = max(test1_marks, test2_marks, course_work_marks)
    average_test_mark = (best_test_mark / 30) * 0.4 
    exam_mark = exam_mark *0.6
    final_score = average_test_mark + exam_mark
    return final_score
final_score = calculate_final_marks("Athens", 83, 80, 85, 90)
print(f"final_score for Athens is {final_score}")


def calculate_final_marks(name, test1_marks, test2_marks, course_work_marks, exam_mark):
    best_test_mark = max(test1_marks, test2_marks, course_work_marks)
    average_test_mark = (best_test_mark / 30) * 0.4 
    exam_mark = exam_mark *0.6

# if-else statement is used when decision has to be among two alternatives
# if-elif-else statement is used when decision has to be made among morethan two alternatives
x =5
if x == 5:
    print("x is 5")
elif x < 5:
    print("x is less than 5")
else:
    print("x is greater than 5")

#Data types in python

#using append and pop and length of the list
colors = ["red", "green", "blue"]
print(colors)
first_colors = colors[0]
print(first_colors)
colors.append("yellow")
print(colors)
colors.pop(0)
print(colors)
num_colors = len(colors)
print(num_colors)

# sequence
num1, num2, num3 = 100, 300, 500
numbers = [100, 300, 500]
numbers1 =[num1, num2, num3]
numbers2 =[]
# a list in python is a collection of values in one single variable/location and we identify it with square brackets
print(type(num1))
things =[100, "hello", 300.0, True,[1, 2, 3]]
print(numbers[2])
print(things[1])
print(things[4][2])
trouble =[20, [30, [100,20, [500]]]]
print(trouble[1][1][2][0])
trouble.append(40)
print(trouble)
trouble.pop()
print(trouble)

#tuple are read only you cannot add anything or remove anything
mytuple =(100, 300, 500)
Capitalcity = {'Uganda': 'Kampala', 'Kenya': 'Nairobi', 'Rwanda': 'Rwand'}
print(Capitalcity['Kenya'])


