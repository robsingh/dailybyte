import json

# Load the inventory
def load_inventory_from_json(filename):
    try:
        with open(filename, 'r') as file:
            inventory = json.load(file)
        return inventory
    
    except FileNotFoundError:
        print(f"{filename} not found! Please verify the path again.")


# Print the inventory
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

# # function to remove an item from a room
def remove_item_from_room(inventory, room, item):
    if room in inventory:
        if item in inventory[room]:
            del inventory[room][item]
            print(f"\nRemoved {item} from {room}.")
        else:
            print(f"Item '{item}' not found in {room}.")
    else:
        print(f"Room {room} not found in the inventory!")


# load the inventory
inventory = load_inventory_from_json(filename='house_inventory.json')

print("Initial Inventory:")
print_inventory(inventory)

add_item_to_room(inventory, "Living Room", "Painting", 250)

remove_item_from_room(inventory, "Bedroom", "Chair")

print("\nUpdated Inventory:")
print_inventory(inventory)

