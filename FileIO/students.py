import csv

name = input("What`s your name? ")
home = input("Where is your home? ")


with open("C:\\Users\\R1d\\PycharmProjects\\FileIO\\students3.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])


with open("C:\\Users\\R1d\\PycharmProjects\\FileIO\\students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})