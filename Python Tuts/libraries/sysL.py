import sys

# take input from the command line
values = sys.argv

if len(values) < 2:
    sys.exit("Too few arguments")
print("Hello my name is:", values[1])


#  slicing the list
#  list[startingIndex : endingIndex]

# slicing the values list starting from 1 to end
for i in values[1:]:
    print(f"the name is {i}")

