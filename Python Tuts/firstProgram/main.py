# this is a comment -- hihi
name = input("Whats your Name? ")
print("Do you love me", name)

# Remove white space from the name & Capitalise the first alphabet
name = name.strip().title()
print(f"Do you love me {name}?")

# split string - returns sequence of character & we can store in multiple variables
first, last = name.split(" ")
print(first)
