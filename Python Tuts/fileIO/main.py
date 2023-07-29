name = input("Whats your name: ")

def main():
    readFile()

# open a file in write mode!
def openFileInReadMode():
    file = open("names.txt","w")
    file.write(f"{name}\n")
    file.close()

# open a file in append mode
def openFileInAppendMode():
    file = open("names.txt","a")
    file.write(f"{name}\n")
    file.close()

# Another way of working with file using "with" keyword
def openFileUsingWithStatement():
    with open("names.txt","a") as file:
        file.write(f"{name}\n")

def readFile():
    with open("names.txt") as file:
        directSort(file)
        

def sortNamesInFile(file):
    names = []
    for line in file:
        names.append(line.rstrip())
    for name in namesList:
        print(name)


# direct sort
def directSort(file):
    for line in sorted(file,reverse=True):
        print(line.rstrip())


if __name__ == "__main__":
    main()