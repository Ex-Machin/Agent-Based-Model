class EnergyAdvisor:
    """
    EnergyAdvisor class, which represents an energy advisor, who can advise a houseowner about the heating system.
    
    Attributes:
        name (str): Name of the energy advisor.
        expertise_level (float): A value between 0 and 1 indicating the level of expertise.
    
    Methods:
        advise(houseowner): Advises the houseowner about the heating system.
            - Advisor can increase the budget (not actual budget, but percieving of the budget), by informing the houseowner about the cost of the heating system
            - Advisor can increase the concern, by informing the houseowner about the environmental impact of the heating system
            - Advisor can increase the preference, by informing the houseowner about the efficiency of the heating system
    """
    def __init__(self, name, expertise_level):
        self.name = name
        self.expertise_level = expertise_level

    def advise(self, houseowner):
        print(f"{self.name} advises {houseowner.name}")
        influence_factor = self.expertise_level / 10
        houseowner.budget *= (1 + influence_factor * 0.05)
        houseowner.environmental_concern += influence_factor * 0.1
        houseowner.efficiency_preference += influence_factor * 0.1