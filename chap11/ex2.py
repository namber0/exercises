class Student:
    def __init__(self, student_card, name):
        self.card = student_card
        self.name = name
        self.grade_average = 0
        self.rank = ""
    
    def get_apa(self, list):
        sum =0
        for grade in list:
            sum = sum + grade
        self.grade_average = sum / len(list)
    
    def set_rank(self):
        if self.grade_average >= 3.6 and self.grade_average <= 4.0:
            self.rank = "Excellent"
        if self.grade_average >= 3.2 and self.grade_average < 3.6:
            self.rank = "Great"
        if self.grade_average >= 2.5 and self.grade_average < 3.2:
            self.rank = "Good"
        elif self.grade_average >= 2.0 and self.grade_average < 2.5:
            self.rank = "Average"
        elif self.grade_average >= 1.0 and self.grade_average<2.0:
            self.rank = "Not good"
        elif self.grade_average < 1.0:
            self.rank = "Bad"

    def __repr__(self):
        return "Name: {}\n Studen ID: {}\n Your average GPA {}\n Your rank: {}".format(self.name, self.card, self.grade_average, self.rank)


student_card = input("Enter the student card: ")
name = input("Enter your full name: ")

list = []
numbers = int(input("Enter number of grade: "))
for number in range(1, numbers + 1):
    grade = float(input("Enter the grade {}: ".format(number)))
    list.append(number)    

student_1 = Student(student_card, name)
student_1.get_apa(list)
print(student_1)
