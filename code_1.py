# This is an example of a nested lists, lists inside 
class_marks = [10, 12, [20, 15, [25, 27]]]
print(class_marks[2][2][0]) #To print 25 in the list
class_marks.append(40) #To add 40 on the list
class_marks.pop() #To remove 40 from the list

#another example
colors = ["red", "green", "blue"]
print(colors)
first_colors = colors[0]
print(first_colors)
colors.append("yellow")
print(colors)
colors.pop(0)
print(colors)
num_colors = len(colors) #To get the total of items
print(num_colors)

# if-else statement is used when decision has to be among two alternatives
# if-elif-else statement is used when decision has to be made among morethan two alternatives
x =5
if x == 5:
    print("x is 5")
elif x < 5:
    print("x is less than 5")
else:
    print("x is greater than 5")
    #output: "x is 5"