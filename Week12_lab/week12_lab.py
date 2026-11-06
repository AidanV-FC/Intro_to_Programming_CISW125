#lists

shopping_cart=["milk", "eggs", "bread", "butter", "cheese", "cereal", "apple", "potato"]
print(len(shopping_cart))

print(shopping_cart[0])
print(shopping_cart[3])
print(shopping_cart[4])
print("these items are dairy products")

shopping_cart.append("heavy cream")
print(shopping_cart)

shopping_cart.insert(7, "apple")
print(shopping_cart)

#list methods

print(shopping_cart.count("apple"))

shopping_cart.remove("milk")
print(shopping_cart)
print("the milk was expired so it was removed from the list")

shopping_cart.sort()
print(shopping_cart)

shopping_cart.reverse()
print(shopping_cart)





#dictionaries
produce_inventory={
    "apples" : 10,
    "peaches" : 8,
    "bananas" : 12,
    "onions" : 15,
    "potatoes" : 20,
    "tomatoes" : 9
}

print(produce_inventory["onions"])

produce_inventory["oranges"] = 10
print(produce_inventory)

produce_inventory["apples"] += 5
print(produce_inventory)

print(produce_inventory.keys())

print(produce_inventory.values())

#iterating through a dictionary
for key in produce_inventory.keys():
    print(key)

for value in produce_inventory.values():
    print(value)

for key, value in produce_inventory.items():
    print(f"{key} : {value}")

#nested dictionaries

customer_order={
    "order1" : { 
        "name" : "Jerry Smith",
        "order" : ["apples", "peaches", "bananas"],
        "total Spent" : 15.25
    },
    "order2" : {
        "name" : "Rebecca Williams",
        "order" : ["bananas", "onions", "potatoes"],
        "total Spent" : 22.50
    },
    "order3" : {
        "name" : "Grant G. Grahamson",
        "order" : ["tomatoes", "onions", "apples"],
        "total Spent" : 18.75
    }
}

print (customer_order["order1"]["name"])
print (customer_order["order2"]["order"])
print (customer_order["order3"]["total Spent"])