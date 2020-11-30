array_input = input("Enter a List of Numbers: ")
split = array_input.split(" ")
for x in range(0, len(split)-1):
    if not(split[x].isnumeric()):
        print("Not an integer")
    else:
        if int(split[x]) > 5:
            print("%d is greater than 5" % int(split[x]))
        if int(split[x]) < 5:
            print("%d is less than 5" % int(split[x]))
