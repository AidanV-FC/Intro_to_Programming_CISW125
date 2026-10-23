#Functions
#What is a function?
#A function is a named set of instructions that performs a specific task.
#Functions let us write code once and reuse it when needed.

#Def(define): creates a function by starting with the keyword def, followed by the function name and parentheses.
#Call: a function by using the function name followed by parentheses.
#Arguments: values that are passed into a function when it is called. They are used to provide input to the function.
#Parameters: variables that are defined in the function definition and are used to receive the arguments passed to the function.

#Create a function that says hello
def hello():
    print("Hello!")
#Call the function
hello()

#define tells python that a function is being created
#Code inside the function must be indented
#Nothing runs until it is called

# #Parameters and Arguments
# def greet(name):
#     #name is a parameter(a placeholder)
#     print(f"Hello, {name}!")
# name = input("What is your name? >")
# greet(name)
# greet("Joe")
#parameters are like blanks. Arguments fill them in.

#The only time you need parameters is when you want to pass information from outside the function into the function.
# def greet():
#     name=input("What is your name? >")
#     print(f"Hello, {name}!")
# greet()

#print vs return
#a function that prints
# def hello_print():
#     print("Hello!")
# #this shows the text to the user#
# # it doesn't give a value back to the rest of the program

# #A function that returns
# def hello_return():
#     name=input("Enter your Name: >")
#     return f"Hello, (name)."
# #This sends a value back to whatever function is called
# #The caller can store it, print it, etc.

# msg=hello_return()
# print(msg)

# result=hello_print()
# print(result) #This will print "None" because hello_print dosen't return a value back to the function

#Print is for the user, return is for the program

#Function example
#Calculator Program

# def calc(num1,num2):
#     operator=input("Input Operator (+, -, *, /:  >")
#     if operator=="+":
#         return num1+num2

# print(calc(1,3))

#fake loop
#A function can called itself. This is called reccursion
#A function can behave like a loop if it repeats until a condition is met
#If a function is calling itself, it must have a stop condtition

#A function that prompts user if they want to continue
def play_again():
    answer=input("Play Again? (y/n):  >").lower()
    if answer=="y":
        play_again() #Cals itself again
    else:
        print("Bye!")
play_again()