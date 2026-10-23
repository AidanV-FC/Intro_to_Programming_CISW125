#PART 1
def greet_user(name):
    print(f"Hello, {name}!")
name=input("Enter Name Here: >")
greet_user(name) #input
greet_user("Joe") #static output

#PART 2
def function_calc(num1,num2):
    operator=input("Enter Operator (+, -, *, /):  >")
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        return num1/num2
    else:
        return "Invalid Operator."
    
num1=int(input("Enter First Number:  >"))
num2=int(input("Enter Second Number:  >"))
print(function_calc(num1,num2))

#PART 3
def fav_food():
    food=input("What is your favorite food?  >")
    return f"Your favorite food is {food}! Yum!"
msg = fav_food()
print(msg)

#PART 4
def continue_task():
    answer=input("Would you like to continue this task? (y/n):  >")
    if answer=="y":
        continue_task()
    elif answer=="n":
        print("Task Cancelled.")
    else:
        print("Invalid response.")
        continue_task()
continue_task()

#PART 5
    #1.) I think I found the print and return function a little confusing.
    #2.) Yeah, I'd say so. I think that functions are best used for code that needs to be referenced later without it having to be rewritten.
    #3.) Nah, not really.