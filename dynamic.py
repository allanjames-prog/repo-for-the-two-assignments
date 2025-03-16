#DYNAMIC FUNCTIONS where variables are expected at the call of it
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
    average_test_mark = (best_test_mark / 2) * 0.4 
    exam_mark = exam_mark *0.6
    final_score = average_test_mark + exam_mark
    return final_score
final_score = calculate_final_marks("Athens", 83, 80, 85, 90)
print(f"final_score for Athens is {final_score}")


def calculate_final_marks(name, test1_marks, test2_marks, course_work_marks, exam_mark):
    best_test_mark = max(test1_marks, test2_marks, course_work_marks)
    average_test_mark = (best_test_mark / 2) * 0.4 
    exam_mark = exam_mark *0.6
    final_score = average_test_mark + exam_mark
    return final_score
final_score = calculate_final_marks("Philmon",75, 85, 90, 92 )
print(f"final_score for Philmon is {final_score}")



