students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i, students[i])


for i, student in enumerate(students):
    print(i, student)

    """
    Output is the same
    """