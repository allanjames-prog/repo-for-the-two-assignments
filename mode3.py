def students_details():
    print("---------------------------")
    print("WELCOME TO STUDENTS RECORDS")
    print("---------------------------")
    print("PLEASE ENTER STUDENTS DETAILS")
    print("---------------------------")
    students_list = []
    num = int(input("Enter number of students entries: "))
   
    for _ in range(num):
        students ={}
        students["name"] = (input("Enter students name\n"))
        students["age"] = int(input("Enter students age\n"))
        students["gender"] = (input("Enter students gender\n"))
        students["school"] = (input("Enter name of school\n"))
        students["program"] = (input("Enter your program\n"))
        students["yearofstudy"]  = int(input("Enter students year of study\n"))
        students["test1"]  = int(input("Enter test1 marks\n"))
        students["test2"]  = int(input("Enter test2 marks\n"))
        students["coursework"]  = int(input("Enter coursework marks\n"))
        students["exam"]  = int(input("Enter your exam mark\n"))
        students["bestmark"]  = bestmark(students["test1"], students["coursework"])
        students["finalmark"]  = finalmark(students["bestmark"], students["exam"])

        students_list.append(students)
    return students_list

def bestmark(test1, coursework):
            return (test1 + coursework)/2*0.4

def finalmark(bestmark, exam):
            return (bestmark)+(exam*0.6)


students_perfomance = students_details()
for student in students_perfomance:
     print(student)

    
