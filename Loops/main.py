def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Provide a positive number:\n"))
        if n <= 0:
            continue
        else:
            return n


def meow(n):
    for _ in range(n):
        print("Meow!")


#List
students = ["Ron", "Harry", "Hermione", "Draco" ]
#Dictionary
houses = {
        "Ron":"Gryfindor",
        "Harry":"Gryfindor",
        "Draco":"Slytheryn",
        "Hermione":"Gryfindor",
        }
#List of dictionaries

detailedStudents = [
    {"Name":"Ron","House":"Gryfindor","Patronus":"Terrier"},
    {"Name":"Hermione","House":"Gryfindor","Patronus":"Otter"},
    {"Name":"Harry","House":"Gryfindor","Patronus":"Stag"}
]



#Lists
def get_students(students):
    for i in range(len(students)):
        print([i],students[i])

#Dictionaries
def get_houses(houses):
    for student in houses:
        print(student,houses[student], sep=" ")


#List of dictionaries
def get_detailedStudents(detailedStudents):
    for student in detailedStudents:
        print("List of dictionaries: ",student["Name"],student["House"],student["Patronus"], sep=" ")

def print_square(size):
    for _ in range(size):
        print("#"*size)

main()
get_students(students)
get_houses(houses)
get_detailedStudents(detailedStudents)
print_square(3)