#PART 1
# with open("Week9_lab/wk9_lab.txt", "w") as file:
#     file.write("this is line 1\n")
#     file.write("this is line 2\n")
#     file.write("this is line 3\n")

# #PART 2
# #reading with a for loop
# with open("Week9_lab/wk9_lab.txt", "r") as file:
#     for line in file:
#         print(line)

# #reading with a variable
# with open("Week9_lab/wk9_lab.txt", "r") as file:
#     contents = file.read()
#     print(contents)

# #PART 3
# with open("Week9_lab/wk9_lab.txt", "a") as file:
#     file.write("this is line 4\n")
#     file.write("this is line 5\n")

# #PART 4
# with open("Week9_lab/wk9_lab.txt", "r") as file:
#     for line in file:
#         print(line)

#Challenge
#creating a file history for the black hole calculator

print("This Program will calculate the mass of a black hole.")

event_horizon = float(input("Enter black hole event horizon radius in kilometers: >"))
m = event_horizon * 1000 #converts kilometers to meters
c = 299792458 #approximate speed of light in m/s
g = 6.67430e-11 #gravitational constant 
mass = (m * c**2) / (2 * g) #calculate
solar_mass = mass // 1.989e30 #convert to solar masses. floor divided to prevent really long decimal.
#note: any black hole under 3 km will be calculated as 0 solar masses due to the floor division.
with open("Week9_lab/black_hole_history.txt", "a") as file:
    file.write(f"Event Horizon: {event_horizon} km, Mass: {mass} kg, Solar Masses: {solar_mass}\n")
print(f"The mass of your black hole is: {mass} kg or approximately {solar_mass} solar masses.\nOr in other words, a really big number!")
