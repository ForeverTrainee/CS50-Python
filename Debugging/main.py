#Using print is friend for debugging :)

def main():
    height = int(input("Height:"))
    pyramid(height)
def pyramid(n):
    for i  in range(n):# we can follow variable values in debugger
        print("#" * (i+1))


if __name__ == "__main__":
    main()
    print("hi")#breakpoint, it will excecute till this, and then i can start it manually
