class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is from {self.house}"


def main():
    student = getStudent()
    print(student)


def getStudent():
    name = input("Enter the name")
    house = input("Enter the house")
    return Student(name,house)


if __name__ == '__main__':
    main()