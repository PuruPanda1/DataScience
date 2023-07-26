def main():
    listWithDictionary()


def dictionaryTool():
    students = {"Purab": "Red House", "Akash": "Blue House", "Sonu": "Green House"}

    #  to access the student house
    print(students["Purab"])

    for s in students:
        print(f"{s} Student is in {students[s]}")


def listWithDictionary():
    students = [
        {"name": "Purab", "Department": "CSE"},
        {"name": "Akash", "Department": "AI & ML"},
        {"name": "Sonu", "Department": "ISE"},
        {"name": "Raja", "Department": "ECE"},
    ]

    for student in students:
        print(student)


main()
