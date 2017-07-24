class Students(object):
    def __init__ (self, student, marks):
        self.student = student
        self.marks = marks

class_report = open("Class_report.txt", "a+")

with open("Class_report.txt", "a+") as class_report:
    while True:
        student = input("Enter a student name, or press enter to exist").strip()

        if not student:
            break

        print ("How many marks did the student get in this exam?")
        marks = input()
        marks = int(marks) 
        if marks >= 80:
            marks = str(marks)
            marks = "an A"
        elif marks >= 70:
            marks = str(marks)
            marks = "a B"
        elif marks >= 60:
            marks = str(marks)
            marks = "a C"
        elif marks >= 50:
            marks = str(marks)
            marks = "a D"
        elif marks < 50 and marks >= 0:
            marks = str(marks)
            marks = "a Fail"

        pupil = Students(student, marks)
        class_report.write(("%s achieved %s" % (pupil.student, pupil.marks)) + "\n")
        

