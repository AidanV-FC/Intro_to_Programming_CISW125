#updated black hole calculator

def claculator():
    event_horizon = float(input("Enter black hole event horizon radius in kilometers: >"))
    m = event_horizon * 1000 #converts kilometers to meters
    c = 299792458 #approximate speed of light in m/s
    g = 6.67430e-11 #gravitational constant 
    mass = (m * c**2) / (2 * g) #calculate
    solar_mass = mass // 1.989e30 #convert to solar masses. floor divided to prevent really long decimal.
    print(f"The mass of your black hole is: {mass} kg or approximately {solar_mass} solar masses.\nOr in other words, a really big number!")
    save_history = input("Would you like to save this calculation to the history file? (y/n): >")
    if save_history.lower() == "y":
        with open("Project4/black_hole_history.txt", "a") as file:
            file.write(f"Event Horizon: {event_horizon} km, Mass: {mass} kg, Solar Masses: {solar_mass}\n")
    elif save_history.lower() == "n":
        print("")
    else:
        print("Invalid Key. Please enter 'y' or 'n'.")
 


def history_viewer():
    with open("Week9_lab/black_hole_history.txt", "r") as file:
        for line in file:
            print(line)

def main_menu():
    print("Welcome to Black Hole Calculator 2.0!")
    options = input("Select an option:\n1. Calculate Black Hole Mass\n2. View Calculation History\n3. Exit\n>")
    if options == "1":
        claculator()
        main_menu()
    elif options == "2":
        history_viewer()
        leave = input("press any key to return to the main menu: >")
        if leave:
            main_menu()
    elif options == "3":
         print("Goodbye!")
    else:
        print("Invalid option. Please select 1, 2, or 3.")
        main_menu()
main_menu()
