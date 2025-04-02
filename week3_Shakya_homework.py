class Student :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.grades = []       #empty list to store grades this was important
        

    def add_grade(self, grade):
        self.grades.append(grade)
        #return grades                         #no need to return

    def calculate_average(self):
        total = 0
        length = len(grades)
        if length > 0:
            for i in grades:
                total += i
            avg = total/length
        return avg

    def get_student_info(self):
        return f"Student(name = {self.name},age = {self.age}, grades = {self.grades})"
