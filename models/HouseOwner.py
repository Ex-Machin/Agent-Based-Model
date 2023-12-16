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
            based on the houseowner's preferences.
        
        calculate_score(system): Calculates a score for a heating system based on
            the houseowner's preferences.
    """

    def __init__(self, name, budget, environmental_concern, efficiency_preference):
        self.name = name
        self.budget = budget
        self.environmental_concern = environmental_concern
        self.efficiency_preference = efficiency_preference

    def calculate_score(self, system):
        return (system.price() / self.budget) + \
                (system.co2_emissions * self.environmental_concern) - \
                (system.energy_efficiency * self.efficiency_preference)

    def choose_heating_system(self, systems):
        # Adjust the selection criteria based on the houseowner's preferences
        best_option = None
        best_score = float('inf')

        for system in systems:
            score = self.calculate_score(system)
            if score < best_score:
                best_score = score
                best_option = system

        return best_option