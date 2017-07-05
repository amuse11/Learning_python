#Simple program that converts the marks of an exam to a grade
print ("How many marks did you get in this exam?")

marks = input()

if marks.isdigit():     #This will check if the input of marks is a digit, if not it will simply end the program with no result
    marks = int(marks)  #This will convert the input of marks into integer form to allow boolean operators to compare
    if marks >= 80:
        print ("Congratulations! You got an A")
    elif marks >= 70:
        print ("Congratulations! You got a B")
    elif marks >= 60:
        print ("You got a C")
    elif marks >= 50:
        print ("You got a D")
    elif marks < 50 and marks >= 0:  #This will check if marks is less than 50, but also at least 0, as you cannot score less than 0 in an exam
        print ("Sadly, you have failed this exam")


