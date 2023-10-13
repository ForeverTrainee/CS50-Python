import sys

def meow(n: int) -> str :
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")


if len(sys.argv) == 1:
    print("Meow!")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("Meows?")
else:
    print("usage: mypy.py")