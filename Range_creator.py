start = int(input("What will be the start of the list?" ))
stop = int(input("What will be the end of the list? ")) + 1
step = int(input("What do you want each number to be incremented by? "))

print(list(range(start,stop, step)))
