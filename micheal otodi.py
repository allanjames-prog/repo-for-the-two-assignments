def get_student_details():
    """Function to collect student details dynamically"""
    print(("\n:wave: Welcome to the Student Mark Calculator!"))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course name: ")
    gender = input("Enter gender (M/F): ")
    year_of_study = int(input("Enter year of study: "))
    
    # Collect marks
    test1 = float(input("Enter Test 1 mark: "))
    test2 = float(input("Enter Test 2 mark: "))
    coursework = float(input("Enter Coursework mark: "))
    exam = float(input("Enter Exam mark (out of 60): "))
    
    return name, age, course, gender, year_of_study, test1, test2, coursework, exam

def calculate_final_mark(test1, test2, coursework, exam):
    """Function to calculate the final mark based on the best two of test1, test2, and coursework"""
    best_two = sorted([test1, test2, coursework], reverse=True)[:2]  # Select top two marks
    best_two_avg = sum(best_two) / 2  # Compute average of best two
    best_two_scaled = (best_two_avg / 100) * 40  # Scale to 40
    
    final_mark = best_two_scaled + exam  # Summation of scaled best two and exam
    return final_mark

def main():
    """Main function to run the program"""
    # Get student details
    name, age, course, gender, year_of_study, test1, test2, coursework, exam = get_student_details()
    
    # Calculate final mark
    final_mark = calculate_final_mark(test1, test2, coursework, exam)
    
    # Display student details and final mark
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Gender: {gender}")
    print(f"Year of Study: {year_of_study}")
    print(f"Final Mark: {final_mark:.2f} / 100")
if __name__ == "__main__":
    main()