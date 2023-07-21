def main():
    # whileLoop()
    # forLoop()
    iterateOverTheList()


def whileLoop():
    i = 0
    while i < 3:
        print("hey")
        i = i + 1
    print("While Loop completed!")


def forLoop():
    for i in [0, 1, 2]:
        print("hey")
    print("For Loop Completed!")


def forLoopWithRange():
    for _ in range(3):
        print("hey")
    print("Loop with Range Completed!")


def iterateOverTheList():
    students = ["Purab", "Priyash", "Someone"]
    for s in students:
        print(s)


main()
