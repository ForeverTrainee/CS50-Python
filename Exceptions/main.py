# print("hello world) - Syntax error

# x - int(input("What`s x?")) - user input "cat" - Value error
# print(f" x is {x}") - Value error


#Try Catch as get_int() function - less code then below

def get_int():
    while True:
      try:
            return int(input("What`s x? "))
      except ValueError:
            #print("X is not an integer") - we can use print to log, or use keyword pass to jus repeat try
            pass


'''
Alternative return in get_int() function, more code hovever more readable


def get_int():
    while True:
      try:
            x = int(input("What`s x? "))
            break
      except ValueError:
            print("X is not an integer")
    return x



#Alternative try catch block

while True:
    try:
        x = int(input("What`s x? "))        
    except ValueError:
        print("X is not an integer")
    else:
        break
print(f"x is {x}")

'''

x = get_int()
print(f"Our x value is: {x}")


'''
Alternative with functional argument - passing string as argument

def get_int(prompt):
    while True:
      try:
            return int(input(prompt))
      except ValueError:
            #print("X is not an integer") - we can use print to log, or use keyword pass to jus repeat try
            pass

x = get_int("What`s x? ")
'''