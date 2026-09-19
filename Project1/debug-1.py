# Intro to Programming
# Debug Exercise 2

# This program should add three numbers together.

total = 0
num1 = int(input("What's the first number? >")) #added int() to convert input to integer
#removed total variable from line 8 since it wasn't necessary
num2 = int(input("What's the second number? >")) #added int() to convert input to integer
#removed total variable from line 10 since it wasn't necessary
num3 = int(input("What's the third number? >")) #added int() to convert input to integer
total = num1 + num2 + num3 #changed total variable to be the sum of num1, num2, and num3
print(f"Total is: {total}")