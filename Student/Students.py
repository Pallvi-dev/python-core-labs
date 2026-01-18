class Student:
    def __init__(self, name, course, rollno):
        self.name = name
        self.course = course
        self.rollno = rollno

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"course: {self.course}")
        print(f"rollno: {self.rollno}")
    
    def updateCourse(self, newcourse):
        self.course = newcourse

s = Student("khushi", "BCA", 3)
s.showDetails()
print("Updating course details...")
s.updateCourse("MCA")     
s.showDetails()
