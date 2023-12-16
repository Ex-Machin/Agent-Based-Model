from data.systems import systems
from utils.select_best_heating_system import select_best_heating_system

best_system = select_best_heating_system(systems)
print(f"Best Heating System: {best_system.name}")