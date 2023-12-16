from models.HeatingSystem import HeatingSystem

def select_best_heating_system(systems):
    # Simple criteria: lowest price and CO2 emissions, highest efficiency
    best_option = None
    best_score = float('inf')

    # Convert all inputs to HeatingSystem objects if they are not already
    systems = [HeatingSystem.from_dict(s) if isinstance(s, dict) else s for s in systems]

    # Find the maximum values for each attribute
    max_price = max(system.price() for system in systems)
    max_emissions = max(system.co2_emissions for system in systems)
    max_energy_efficiency = max(system.energy_efficiency for system in systems)

    for system in systems:
        # Normalize the data
        normalized_price = system.price() / max_price
        normalized_emissions = system.co2_emissions / max_emissions
        normalized_efficiency = system.energy_efficiency / max_energy_efficiency

        # Simple criteria: lowest price and CO2 emissions, highest efficiency
        score = normalized_price + normalized_emissions - normalized_efficiency
        if score < best_score:
            best_score = score
            best_option = system

    return best_option