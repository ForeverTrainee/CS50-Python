import sys
def main():
    student = Student.get()
    print(f"{student.name} from {student.house}")


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

#Getter
    @property
    def house(self):
        #Underscore property is like private in "honor system" like python - : do not touch it!
        return self._house
#Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


#Self is reference to current object




def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


def get_student_class():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

# reassign_student_list()
def reassign_student_list():
    student = get_student_list()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]}, from {student[1]}")

    # reassign_student_dictionary()
def reassign_student_dictionary():
    student = get_student_dictionary()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']}, from {student['house']}")


# Tuples
def get_student_tuples():
    name = input("What`s your name? ")
    house = input("What`s your house? ")
    return name, house  # <- this is tuples, we can refer later like student[0] and student[1]
    # we cannot!!! re-assign tuples value for example student[1] = "Gryfindor"
    # we can nest tuples same like lists can be nested


def get_student_list():
    name = input("What`s your name? ")
    house = input("What`s your house? ")
    return [name, house]  # <- return multiple values in list
    # we can!!! re-assign value like student[1] = "Gryfindor"


def get_student_dictionary():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}  # <- return values in dictionary, we can change values in dict


if __name__ == "__main__":
    main()
