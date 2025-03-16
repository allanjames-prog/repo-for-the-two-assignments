def student_details ():
    num = int(input("enter the number of enteries"))
    dict ={input("enter a key:"):input("enter a value") for _ in range(num)}
   # print(dict)
#student_details()

def test():
    num1 = int(input("enetr test1 mark:\n"))
    num2 = int(input("enter test2 mark\n"))
    return(num1 + num2)/2*0.4
print(test())

def final_exam():
    num3 = int(input("final exam marks:\n"))
    return num3 *0.6
print(final_exam())

def total_marks():
    num3 = int(input("test marks"))
    num4 = int(input("enter final_exam"))
    return num3 + num4
print(total_marks())