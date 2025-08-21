class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
    def calculate_grade(self):
        if 90 <= self.marks <= 100:
            return 'A'
        elif 75 <= self.marks <= 89:
            return 'B'
        elif 60 <= self.marks <= 74:
            return 'C'
        else:
            return 'Fail'
# Take input from user
name = input("Enter your name: ")
roll_no = input("Enter your roll number: ")
marks = int(input("Enter your marks: "))
student = Student(name, roll_no, marks)
student.display_details()

