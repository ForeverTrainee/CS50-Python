students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
gryffindors2 = {student: "Gryffindor" for student in students}


print(gryffindors)
"""
print(gryffindors) output
[{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, 
{'name': 'Ron', 'house': 'Gryffindor'}]

"""
print(gryffindors2)
"""
print(gryffindors2) output
{'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}
"""
