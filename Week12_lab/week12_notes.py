# # Notes

# #making a list
# favgames=["Doom", "Quake", "Space Marine"]

# #indexing a list
# #searching through a list via its placement
# print(favgames[0])
# print(favgames[1])
# print(favgames[2])

# #using len() with a list
# print(len(favgames))

# #adding items to a list
# #append adds items to an end
# #insert() adds an item to a specific position

# favgames.append("Fear")
# print(len(favgames))

# #inserting a list item in a certain position
# favgame.insert(0, "Black")
# print(favgames)

# #Common list methods
# #count() counts how many times a value appears
# #sort() puts the list into a sorted order

# #count
# print(favegames.count("Quake"))
# print(favgames)

# #remove
# favgames.remove("Space Marine")
# print(favgames)

# #sort
# favgames.sort()
# print(favgames)

# #reverse() example
# favgames.reverse()
# print(favgames)

# #looping through a list

# for game in favgames:

# #dictionaries


# player_stats={
#     #key : values
#     "Health" : 250,
#     "Armor" : 150,
#     "Speed" : 8,
#     "Starting Weapon" : "Chainaxe"
# }
# #a dictionary stores data in key value pairs

# #how to access data from a dictionary
# print(player_stats["Health"])

# #adding and updating dictionary values
# player_stats["Strength"] = 12
# print(player_stats)

# #updating a value
# player_stats["Health"]=300

# #adding a value
# player_stats["speed"]+2
# print(player_stats)

#keys and values
#keys shows all dictionary keys
#values shows all dictionary values

# for key in player_stats.keys():
#     print(key)

# for value in player_stats.values():
#     print(value)

# for key, value in player_stats.items():
#     print(f"{key} : {value}")

#nested dictionaries
# students={
#         "001":{
#             "name": "John", 
#             "major": "Computer Science", 
#             "credits": 12
#             },
#         "002":{
#                 "name": "Jane", 
#                 "major": "Mathematics", 
#                 "credits": 15
#                }
            

#           }

# print(students["001"]["name"])

#combining a nested dictionary with a list
cars={
    "Toyota": {
        "country" : "Japan",
        "year" : 1937,
        "models": ["Camry", "Corolla", "Prius"]
    }
    }