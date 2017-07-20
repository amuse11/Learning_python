start = int(input("What will be the start of the list?" ))
stop = int(input("What will be the end of the list? ")) + 1
step = int(input("What do you want each number to be incremented by? "))

while stop < start:
    print ("The end of the list is smaller than the start, choose a different end of the list, please.")
    stop = int(input("What will be the end of the list? ")) + 1

print(list(range(start,stop, step)))
