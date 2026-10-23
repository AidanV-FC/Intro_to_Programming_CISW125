# #loops
# #loops repeat code
# # Python uses for and while loops

# #repeat this loop 3 times
# for number in range(3):
#     print("Hello")




# #while loop
# # A while loop will continue to run as long as a condition is true
# number = 1
# #keep looping while number is less than or equal to 5
# while number <= 5:
#     print(number)
#     number += 1 #this is the same as number = number + 1

# #make sure something changes in the while loop or it will run forever

# #while loops with user input
# # a while loop is useful when you want to keep asking the user for input until they give you a valid answer


# #ask user for their age
# age = int(input("What is your age? >"))
# #keep looping if the age is less than 1 or greater than 120
# while age < 1 or age > 120:
#     print("Please enter a valid age")
#     age = int(input("What is your age? >"))
# #this runs after loop finishes
# #loop stops once condition is false
# print("age is valid")

# #for loopswork through item one at a time
# games = ["hexen", "quake", "blood", "doom", "half life", "duke nukem"]
# for game in games:
#     print(game)

# #using range
# #range is a fsequence of numbers

# #start at 2 and stop at 8
# for number in range(2, 8): #2 is our starting point is 8 is where we stop (not included)
#     print(number)
#     # the end number is not included in the range, so it will print 2,3,4,5,6,7

# #loop 2 - 7
# for number in range(2, 8):
#     #multiply the number by itself
#     square = number * number
#     print(square)

# #looping through strings
# # A string can be loop through one one character at a time
# #store a string value inside a variable
# word = "super"
# #take each character in the string and store it in a variable called letter
# for letter in word:
#     print(letter) #prints current letter

# # Using breaks
# #break stops a loop from running
# #loop through numbers 1 - 10
# for i in range(1, 11):
#     #print the current number
#     print(i)
#     #stop the loop when the number is 5
#     if i == 5:
#         break #stops the loop

# #nested loops
# #nested loop is a loop inside another loop
# #outer loop will loop through numbers 1 - 3
# for number in range(1, 4):
#     #inner loop also loops through numbers 1 - 3
#     for inner_number in range(1, 4):
#         #print the current number and inner number
#         print(number, inner_number)

#choosing the right loop
#use a while loop when repetition is based on a condition
#keep looping while answer is not yes
answer = input("Do you want to continue? (y/n) >")
while answer != "y":
    print("Please enter 'y' to continue")
    answer = input("Do you want to continue? (y/n) >")

#use for loop when you know how many times you want to repeat something
#go through each item in a list and print it
itemlist = []
for item in itemlist:
        print(item)

#use for with range when you want to repeat something a specific number of times
#loop through numbers 1 - 10 and print each number
for number in range(1, 11):
    print(number)