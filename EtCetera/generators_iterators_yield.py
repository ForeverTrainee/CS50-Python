def main():
    n = int(input("What`s n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑 " * i
    """
    Point of using yield instead of return:
    if we use return we return every value, 1 sheep, 2 sheep... 100000 sheeps
    this may kill your memory and program will broke
    if use yield loop still works however we will return only final value for example 1 milion sheeps
    so our program will still work/
    """

if __name__ == "__main__":
    main()