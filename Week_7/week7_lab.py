#PART 1

#basic while loop that counts to 5
count = 1
while count <= 5:
    print(count)
    count += 1


#PART 2

#loop that uses user input
percentage = int(input("What is your percentage? >"))
while percentage < 0 or percentage > 100:
    print("Please enter a valid percentage")
    percentage = int(input("What is your percentage? >"))


#PART 3

#basic for loop
list = ["black hole", "pulsar", "hypergiant", "neutron star", "quasar"]
for item in list:
    print(item)


#PART 4

#for loop with range
for i in range(1, 6):
    print(i)


#PART 5

#loop through a string
name = "Aidan"
for letter in name:
    print(letter)


#PART 6

#loop that prints 1 - 10 and breaks early
for i in range(1, 11):
    print(i)
    if i == 7:
        break


#PART 7

#nested loops
for num in range(1, 4):
    for inner_num in range(1, 4):
        print(num, inner_num)
        #The loop outputs 9 times due to the inner loop running 3 times for each iteration of the outer loop.
