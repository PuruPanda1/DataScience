def main():
    print(get_int())


#  else prints n value when there is not exception
def exception():
    try:
        n = int(input("Enter the number: "))
        print(f"The number is {n}")
    except ValueError:
        print("The value of n is not correct")
    else:
        print(f"The number is {n}")


# get the integer even after incorrectinput/exception using while loop
def get_int():
    while True:
        try:
            return int(input("Enter the number: "))
        except ValueError:
            print("Not an Integer")


# pass - dont do anything when exception is received

def pass_function():
    try:
        return int(input("Enter the number: "))
    except ValueError:
        pass


main()
