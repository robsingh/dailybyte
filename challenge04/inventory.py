house_inventory = {
    "Living Room": {
        "TV": 400,
        "Couch": 800,
        "Coffee Table": 150,
        "Bookshelf": 200,
        "Lamp": 50
    },
    "Bedroom": {
        "Bed": 1000,
        "Wardrobe": 500,
        "Desk": 250,
        "Chair": 100,
        "Nightstand": 75
    },
    "Kitchen": {
        "Fridge": 1200,
        "Microwave": 150,
        "Oven": 800,
        "Dining Table": 600,
        "Chair": 100
    },
    "Bathroom": {
        "Shower": 700,
        "Toilet": 300,
        "Sink": 150,
        "Cabinet": 200,
        "Mirror": 100
    },
    "Study": {
        "Computer": 1200,
        "Desk": 500,
        "Chair": 200,
        "Bookshelf": 300,
        "Lamp": 75
    }
}

# function to print the inventory
def print_inventory(inventory):
    for room, items in inventory.items():
        print(f"\n{room}:")
        for item,value in items.items():
            print(f"    {item}: ${value}")

# function to add an item to a room
def add_item_to_room(inventory, room, item, value):
    if room in inventory:
        inventory[room][item] = value
        print(f"\nAdded {item} with ${value} to {room}.")
    else:
        print(f"Room {room} not found in the inventory!")

# function to remove an item from a room
def remove_item_from_room(inventory, room, item):
    if room in inventory:
        if item in inventory[room]:
            del inventory[room][item]
            print(f"\nRemoved {item} from {room}.")
        else:
            print(f"Item '{item}' not found in {room}.")
    else:
        print(f"Room {room} not found in the inventory!")


print("Initial Inventory:")
print_inventory(house_inventory)

add_item_to_room(house_inventory, "Living Room", "Painting", 250)

remove_item_from_room(house_inventory, "Bedroom", "Chair")

print("\nUpdated Inventory:")
print_inventory(house_inventory)

