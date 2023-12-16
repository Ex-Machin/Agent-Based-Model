class HeatingSystem:
    def __init__(self, name, price_of_installing, system_cost,  co2_emissions, energy_efficiency, type_of_fuel):
        self.name = name
        self.price_of_installing = price_of_installing  # in thousands
        self.system_cost = system_cost  # in thousands
        self.co2_emissions = co2_emissions  # in tons/year
        self.energy_efficiency = energy_efficiency  # as a decimal
        self.type_of_fuel = type_of_fuel # natural gas, fuel oil, electricity, propane/lpg, wood

    def price(self, years=1):
        return self.price_of_installing + self.system_cost * years
    
    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            name=dict_obj['name'],
            price=dict_obj['price'],
            co2_emissions=dict_obj['co2_emissions'],
            energy_efficiency=dict_obj['energy_efficiency']
        )
