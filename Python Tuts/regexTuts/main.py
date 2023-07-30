# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions

# ^   matches the start of the string
# $   matches the end of the string or just before the newline at the end of the string

# []    set of characters
# [^]   complementing the set

# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character

# A|B     either A or B
# (...)   a group
# (?:...) non-capturing version

import re

def main():
    emailChecker()


def emailChecker():
    email = input("Enter the Email: ")

    if re.search(r"^\w+@(\w+\.)?\w+\.(edu|in|com)$", email, re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")


# function to format the user's name
def formatData():
    name = input("Enter the your name: ").strip()

    

    print(f"hello, {name}")



if __name__ == '__main__':
    main()

