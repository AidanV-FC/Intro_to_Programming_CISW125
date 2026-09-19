#Planet Fun Facts!

print("Welcome to Planet Fun Facts!")

print("Which planet would you like to know about?")

selection = input("Which planet would you like to know about?\n1. Mercury\n2. Venus\n3. Earth\n4. Mars\n5. Jupiter\n6. Saturn\n7. Uranus\n8. Neptune\n9. Pluto\n> ")
if selection == "1":
    print("Mercury has a large iron core that takes up about 85% of the planet's radius.")
elif selection == "2":
    print("A day on Venus lasts about 243 Earth days, which is longer than its year.")
elif selection == "3":
    print("About 3 billion years ago, Earth was hit by a Mars-sized object that created the Moon.")
elif selection == "4":
    print("Mars has the tallest volcano in the solar system, Olympus Mons, which is about 13.6 miles high.")
elif selection == "5":
    print("Jupiter's core is made from a strange supercritical metallic hydrogen goo.")
elif selection == "6":
    print("Saturn has a strange hexagonal storm at its north pole that has been raging for decades.")
elif selection == "7":
    print("Uranus is the only planet that rotates on its side, making its seasons very extreme.")
elif selection == "8":
    print("Neptune has the fastest winds in the solar system, reaching speeds of over 1,200 miles per hour.")
elif selection == "9":
    print("Pluto is a binary system with its largest moon, Charon, which is about half its size.")
else:
    print("Invalid selection. Please choose a number between 1 and 9.")