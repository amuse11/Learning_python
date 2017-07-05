print ("How many marks did you get in this exam?")

marks = input()

if marks.isdigit():
    marks = int(marks)
    if marks >= 80:
        print ("Congratulations! You got an A")
    elif marks >= 70:
        print ("Congratulations! You got a B")
    elif marks >= 60:
        print ("You got a C")
    elif marks >= 50:
        print ("You got a D")
    elif marks < 50 and marks > 0:
        print ("Sadly, you have failed this exam")


