def select_best_heating_system(options):
    # Simple criteria: lowest price and CO2 emissions, highest efficiency
    best_option = None
    best_score = float('inf')

    for option in options:
        score = option.price() + option.co2_emissions - option.energy_efficiency
        if score < best_score:
            best_score = score
            best_option = option

    return best_option