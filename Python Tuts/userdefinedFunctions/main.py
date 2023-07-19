# creating a function using def keyword
def hello(to="world"):
    print("Hello,", to)


name = input("Whats your name? ")
hello(name)
# will print the default value of the argument in the hello function()
hello()
