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

def print_inventory(inventory):
    for room, items in inventory.items():
        print(f"\n{room}:")
        for item,value in items.items():
            print(f"    {item}: ${value}")


print_inventory(house_inventory)