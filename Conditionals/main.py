def main():
    x = int(input("Provide X number: "))
    y = int(input("Provide Y number: "))
   #IF statement
    if x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{y} is greater than {x}")
    else:
        print(f"{x} is equal {y}")

    #IF with or statement
    if y < x or x < y:
        print("Numbers are not equal")
    elif x == y:
        print("Numbers are equal")

    if y >= 15 and x >= 20:
        print("grade 5")
    elif y >= 0 and x < 5:
        print("grade 1")

    if is_even(x):
        print("Number is even")
    else:
        print("Number is odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


name = input("what is your name?")

match name:
    case "Harry" | "Ron" | "Hermione":
           print("Gryfindor")
    case "Draco":
           print("Slytheryn")
    case _:
            print("Who?")



main()