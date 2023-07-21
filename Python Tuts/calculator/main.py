# num1 = int(input("Enter the number 1: "))
# num2 = int(input("Enter the number 2: "))
#
# print("The output is:", num1 + num2)

# floating number input

# f1 = float(input("Enter the Floating number: "))
# print(f1)
# # round and format the string to the currency!
# print(f"Round number: {round(f1):,}")
#
# # Rounding the number with given number of decimal digits... here its 2
# z = 2 / 3
# print(round(z, 2))
# print(f"{z:.2f}")
#

# using functions and return

def main():
    num1 = int(input("enter the first value"))
    num2 = int(input("enter the second value"))

    print(addition(num1,num2))


def addition(num1, num2):
    return num1 + num2


main()
