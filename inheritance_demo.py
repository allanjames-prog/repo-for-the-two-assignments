# Base class (Parent)
class Person:
    def __init__(self, name, age, gender, nationality, occupation, birthday, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.occupation = occupation
        self.birthday = birthday
        self.phone = phone
    
    def introduce(self):
        return f"My name is {self.name}. I am a {self.occupation} from {self.nationality}."


# Derived class 1 (Inheriting from Person)
class Student(Person):
    def __init__(self, name, age, gender, nationality, occupation, birthday, phone, university, course):
        super().__init__(name, age, gender, nationality, occupation, birthday, phone)
        self.university = university
        self.course = course

    def study(self):
        return f"{self.name} is studying {self.course} at {self.university}."


# Derived class 2 (Inheriting from Person)
class Teacher(Person):
    def __init__(self, name, age, gender, nationality, occupation, birthday, phone, subject, experience):
        super().__init__(name, age, gender, nationality, occupation, birthday, phone)
        self.subject = subject
        self.experience = experience

    def teach(self):
        return f"{self.name} teaches {self.subject} with {self.experience} years of experience."


# Derived class 3 (Inheriting from Student)
class GraduateStudent(Student):
    def __init__(self, name, age, gender, nationality, occupation, birthday, phone, university, course, thesis_title):
        super().__init__(name, age, gender, nationality, occupation, birthday, phone, university, course)
        self.thesis_title = thesis_title

    def research(self):
        return f"{self.name} is researching on '{self.thesis_title}'."


# Derived class 4 (Final class with five methods)
class Principal(Teacher):
    def __init__(self, name, age, gender, nationality, occupation, birthday, phone, subject, experience, school):
        super().__init__(name, age, gender, nationality, occupation, birthday, phone, subject, experience)
        self.school = school

    def manage(self):
        return f"{self.name} is managing {self.school}."

    def hire_teachers(self):
        return f"{self.name} is hiring new teachers for {self.school}."

    def evaluate_teachers(self):
        return f"{self.name} is evaluating teachers at {self.school}."

    def schedule_meetings(self):
        return f"{self.name} is scheduling meetings with school board members."

    def handle_student_issues(self):
        return f"{self.name} is handling student issues at {self.school}."




    # Creating objects with correct country codes in phone numbers
student1 = Student("Dinah Drizella", 20, "Female", "Tanzanian", "Student", "2004-05-15", "+1-123-456-7890", "Harvard", "Computer Science")
teacher1 = Teacher("Mr. Thompson", 45, "Male", "British", "Teacher", "1979-08-22", "+44-987-654-3210", "Mathematics", 15)
principal1 = Principal("Dr. Edward", 55, "Male", "Canadian", "Principal", "1969-12-10", "+1-555-123-4567", "Administration", 25, "Greenwood Academy")

