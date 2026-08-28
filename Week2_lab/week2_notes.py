game="Quake"
print(game)
#this is a comment
player_name="Flying Chainsaw"
number1=5
number2="Flying "
number3="Chainsaw"
print(number2 + number3)

#variable notes
    #variables can't start with numbers
    #variables can't contain spaces
    #vatiables should use lowercase letters
    #variable should correspond with the what the value is

#Variables can change, python is a top-down language
ammo=25
print(ammo)
ammo=50

x=5
y=7
z=x+y
print(z)

fav_team="The San Diego Padres"
#this way is old and smelly
print("My favorite baseball team is " +fav_team+ ". They're the greatest!")
#this way is also old and smelly
print("My favorite baseball team is", fav_team, ". They're the greatest!")

#fprint is much better lmao
print(f"My favorite baseball team is {fav_team}. They're the greatest!")

fav_player="Mookie Betts"
Ws=8
print(f"Despite being a Padres fan, my favorite player is {fav_player}. He won {Ws} games!")

total=9+10
print(total)

# % gives the remainder
total=5%3
print(total)

# ** are for exponents
print(16**2)

# // is for floor division
print(15//2)

price=15
quantity=2
total=price*quantity
print(total)

score=15
score=score+5
print(score)

score+=5
score-+5
score*=5
print(score)