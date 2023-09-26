#Return values and variables

name = "Andrzej"
print(name)
print("My name is: ",name)
#Set variable from input
yourName = input("What is your name?\n")


#Multiple function arguments
separator = ":"
newLine = "\n"
print("1-Your name is"+separator+yourName)
print("2-Your name is",separator,yourName)
print(f"3-Your name is {yourName}")

#String methods

stripString = "   I have white spaces     "
stripString = stripString.strip()
print(stripString)

capitalizeString = "i have capitalized letter "
capitalizeString = capitalizeString.capitalize()
print(capitalizeString)

titleString = "it is title type string"
titleString = titleString.title()
print(titleString)

multipleManipulationString = "    spaces and titles  "
multipleManipulationString = multipleManipulationString.strip().title()
print(multipleManipulationString)


#Int/Float methods
#conversion from prompt(string) to integer
print(int(input("First number"))+int(input("Second number")))

firstNumber = 1.12
secondNumber =2.13
result = round((secondNumber+firstNumber))
print(f"{result}") # return 3

firstNumber = 980
secondNumber = 20
result =  round((secondNumber+firstNumber))
print(f"{result:,}") # return 1,000 with comma separator

firstNumber = 2
secondNumber = 3
result =  round((secondNumber+firstNumber))
print(f"{result:.2f}") # print 5.00 with dota separator


#Defining function

def Hello():
    print("Hello :)")

Hello()

def Hello2(param="Hello World"):
    print("This is paramentr:",param)

passedParamentr = "Hello you!"
Hello2() # return "Hello world" as predefined parametr
Hello2(passedParamentr) # return "Hello you!" as predefined paramentr is changed

def Square(n):
    return n*n
def Calculation():
    x = 5
    print("Square:",Square(x))
Calculation()