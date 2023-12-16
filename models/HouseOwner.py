from models.HeatingSystem import HeatingSystem
from data.weights import PRICE_WEIGHT, EMISSIONS_WEIGHT, EFFICIENCY_WEIGHT

class Houseowner:
    """
    The Houseowner class represents a residential property owner who is considering 
    replacing their heating system. The class includes attributes to represent the 
    houseowner's preferences and methods to make an informed decision based on 
    various criteria such as cost, efficiency, and environmental impact.

    Attributes:
        name (str): Name of the houseowner.
        budget (float): Available budget for the heating system in thousands.
        environmental_concern (float): A value between 0 and 1 indicating the 
            level of concern for environmental impact.
        efficiency_preference (float): A value between 0 and 1 indicating the 
            preference for system efficiency.

    Methods:
        choose_heating_system(systems): Selects the best heating system from a list 
            based on the houseowner's preferences. Using weights for each factor.
        
        calculate_score(system): Calculates a score for a heating system based on
            the houseowner's preferences.

        interact_with_other(other_houseowner): Interacts with another houseowner.
            Can convince the other houseowner to be more environmentally concerned.
    """

    def __init__(self, name, budget, environmental_concern, efficiency_preference):
        self.name = name
        self.budget = budget
        self.environmental_concern = environmental_concern
        self.efficiency_preference = efficiency_preference

    def interact_with_other(self, other_houseowner):
        print(f"{self.name} interacts with {other_houseowner.name}")

        # When the other houseowner is more environmentally concerned, this houseowner will also be more concerned
        if self.environmental_concern > other_houseowner.environmental_concern:
            print(f"{self.name} convince {other_houseowner.name} about environmental concern")
            other_houseowner.environmental_concern += 0.1

    def choose_heating_system(self, systems):
        # Adjust the selection criteria based on the houseowner's preferences
        best_option = None
        best_score = float('inf')

        # Find the maximum values for each attribute
        max_price = max(system.price() for system in systems)
        max_emissions = max(system.co2_emissions for system in systems)
        max_energy_efficiency = max(system.energy_efficiency for system in systems)

        for system in systems:
            # Skip systems that are out of budget
            if system.price() > self.budget:
                continue

            # Normalize the data
            normalized_price = system.price() / max_price
            normalized_emissions = system.co2_emissions / max_emissions
            normalized_efficiency = system.energy_efficiency / max_energy_efficiency

            score = (normalized_price * PRICE_WEIGHT / self.budget) + \
                (normalized_emissions * EMISSIONS_WEIGHT * self.environmental_concern) - \
                (normalized_efficiency * EFFICIENCY_WEIGHT * self.efficiency_preference)
            
            if score < best_score:
                best_score = score
                best_option = system

        if best_option is None:
            return HeatingSystem(name="None", price_of_installing=0, system_cost=0, co2_emissions=0, energy_efficiency=0, type_of_fuel="None")

        return best_option