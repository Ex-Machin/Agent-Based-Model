from data.systems import systems
from models.HouseOwner import Houseowner

john = Houseowner(name="John Doe", budget=5, environmental_concern=0.8, efficiency_preference=0.9)

best_system_for_john = john.choose_heating_system(systems)
print(f"Best Heating System for {john.name}: {best_system_for_john.name}")
