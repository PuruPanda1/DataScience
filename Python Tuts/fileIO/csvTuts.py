import csv

students = []

def main():
    csvDictWriter()


def readCSVFile():
    with open("students.csv") as file:
        for line in file:
            name, address= line.rstrip().split(",")
            student = {"name": name,"address": address}
            students.append(student)
        sortedDictionaryUsingLambda(students)


def sortedDictionaryUsingLambda(students):
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['address']}")


def readingFileUsingCSV():
    with open("students.csv") as file:
        reader = csv.reader(file)
        for name, address in reader:
            students.append({"name":name, "address":address})
        sortedDictionaryUsingLambda(students=students)

def readFileUsingDictReader():
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({
                "name":row['name'],
                "address":row['address']
            })
        sortedDictionaryUsingLambda(students)

def csvWriterTuts():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    with open("students.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow([name,address])

def csvDictWriter():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    with open("students.csv","a") as file:
        writer = csv.DictWriter(file,fieldnames=["name","address"])
        writer.writerow({"name": name, "address": address})

if __name__ == "__main__":
    main()
