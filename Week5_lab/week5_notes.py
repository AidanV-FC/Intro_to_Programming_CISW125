# A boolean is a true or false value.
print(5>10)
print(5<10)
print(10>=20)
print("cat"=="Cat")

# Any expression that evaluates to true or false is a boolean expression.
# if statements are used to decide what to run

answer = input("Do you want to continue? (y/n) >").lower()
if answer == "y":
    print("Continuing program...")
elif answer == "n":
    print("Exiting program...")
else:
    print("Invalid input. Please enter 'y' or 'n'.")

percentage = int(input("What percentage did you get on the test? >"))
if percentage >= 90:
    print("Good Job!You got an A!")
elif percentage == 100:
    print("HOLY SMOKES! You got a P!")
elif percentage >= 80:
    print("Not Bad. You got a B.")
elif percentage >= 70:
    print("You got a C. Did you even try?")
elif percentage >= 60:
    print("Good Job! That was awful. You got a D.")
elif percentage < 60:
    print("Bruh. HOW?")

score = 85
print(score > 75)
print(score < 75)
print(score == 100)

temp = 72
if temp >= 72 and temp <= 75:
    print("It's a nice day!")

# when using 'and' both conditions are true
# When using 'or' at least 1 condition is true

# I would like this program output ("you don't have to go to school today!")
day = "monday"
is_holiday = False
if day == "saturday":
    print("no class today, its saturday")
elif day == "sunday":
    print("no class today, its sunday")
elif is_holiday == False:
    print("no class today, its a holiday")

# Chained Comparisons

score = 75
if 60 <= score < 90:
    print("score is passing, but not perfect.")

# using if + elif + else
# this is a simple 3 catagory example
# this program prints out the shipping cost based on order price
# when using any sort of money, it is best to use float instead of int
total = float(input("Enter order total: >"))
if total < 25:
    print("Shipping cost is $5.00")
elif total >50:
    print("Shipping cost is $2.00")
else:
    print("Shipping cost is $3.00")
# Compare == & is
list1=[1,2,3]
list2=[1,2,3]
list3=list1
print(list1 == list2)  # True  
print(list1 is list2)  # False different objects in memory
print(list1 is list3)  # True same object in memory
# == compares values/content
# 'is' compares identity

#multi branch
#program that tells me if a number is positive or negative
number = int(input("Enter a number: >"))
if number < 0:
    print("negative")
elif number > 0:
    print("positive")
else:
    print("0")