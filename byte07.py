"""
Given the provided cars dictionary:

Get all Jeeps
Get the first car of every manufacturer.
Get all vehicles containing the string Trail in their names (should work for other grep too)
Sort the models (values) alphabetically
See the docstrings and tests for more details. Have fun!    


"""

cars = {"BMW":["BMW3", "BMW5","BMW9","BMWX"],
        'Ford':['Focus','Mustang', 'Bronco Trail','Escape','Expedition Trail'],
        'Mercedes-Benz': ['AMG SL','Roadster', 'AMG'],
        'Toyota':['Camry', 'Prius','Corolla', 'Supra', '4Runner', 'HighLander Trail'],
        'Tesla':['Model 3', 'Model S', 'Model X', 'Model Y', 'Cyber Truck'],
        'Jeep':['Grand Cherokee', 'Wrangler Trail', 'Gladiator', 'Compass Trail', 'Renegade']
        }

def get_all_jeeps(cars):
    return cars.get('Jeep', [])

jeeps = get_all_jeeps(cars)
print("All Jeeps: ", jeeps)


def get_first_car(cars):
    first_cars = [models[0] for models in cars.values()]
    return first_cars

first_cars = get_first_car(cars)
print(f"First Car of each manufacturer: ", first_cars)


def get_vehicles_with_string(cars,search_string):
    matching_vehicles = [model for models in cars.values() for model in models if search_string in model]
    return matching_vehicles

trail_vehicles = get_vehicles_with_string(cars, 'Trail')
print(f"Vehicles containing 'Trail': ", trail_vehicles)


def sort_models(cars):
    sorted_models = {manufacturer: sorted(models) for manufacturer, models in cars.items()}
    return sorted_models


sorted_models = sort_models(cars)
print("Sorted Models: ")
for manufacturer, models in sorted_models.items():
    print(f"{manufacturer} : {', '.join(models)}")