#Black Hole Mass Calculator

print("This Program will calculate the mass of a black hole.")

event_horizon = float(input("Enter black hole event horizon radius in kilometers: >"))
m = event_horizon * 1000 #converts kilometers to meters
c = 299792458 #approximate speed of light in m/s
g = 6.67430e-11 #gravitational constant 
mass = (m * c**2) / (2 * g) #calculate
solar_mass = mass // 1.989e30 #convert to solar masses. floor divided to prevent really long decimal.
#note: any black hole under 3 km will be calculated as 0 solar masses due to the floor division.
print(f"The mass of your black hole is: {mass} kg or approximately {solar_mass} solar masses.\nOr in other words, a really big number!")

#hopefully this works correctly, I think I did the math right. Exponents are kinda weird to work with.