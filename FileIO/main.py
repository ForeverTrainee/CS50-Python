import csv

names = []

'''
#name = input("What`s your name? ")
#file = open("names.txt", "a")

#file.close()

#with open("names.txt", "w") as file:
#    file.write(f"{name}\n")

#for _ in range(3):
#   names.append(input("What`s your name? "))

#for name in sorted(names):
  #  print (f"Hello, {name}")

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.strip())
    #lines = file.readline()
    
    
#for student in sorted(students):
 #   print(student)

#for name in sorted(names, reverse=True):
#    print(f"Hello ",{name})

'''



students = []
students2 = []
students3 = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(house):
    return student["house"]

for student in sorted (students, key=get_house):
    print(f"{student['name']} is in {student['house']}")

#using csv.reader - reult list of collumns
with open("students2.csv") as file:
    reader = csv.reader(file)
    # we can write also for name, home in reader ( csv have to columns
    for row in reader:
        #ifwe use name,home we would use students.append({"name":name, "home":home})
        students2.append({"name": row[0], "home": row[1]})

for student in sorted(students2, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



#using csv.DictReader - result dictionary
with open("students3.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students3.append({"name": row['name'], "home": row['house']})

for student in sorted(students3, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")