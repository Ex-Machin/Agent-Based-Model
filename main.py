from data.systems import systems
from models.HouseOwner import Houseowner
from models.EnergyAdvisor import EnergyAdvisor

john = Houseowner(name="John", budget=10, environmental_concern=0.8, efficiency_preference=0.9)
bill = Houseowner(name="Bill", budget=10000, environmental_concern=0.1, efficiency_preference=1)
andrew = Houseowner(name="Andrew", budget=3, environmental_concern=0.5, efficiency_preference=0.5)
jane = Houseowner(name="Jane", budget=100, environmental_concern=0.9, efficiency_preference=0.9)	

breanly = EnergyAdvisor(name="Breanly", expertise_level=0.8)

def simulate_interactions(houseowners, advisors):
    for owner in houseowners:
        # Houseowners interact with advisors
        for advisor in advisors:
            advisor.advise(owner)

        # Houseowners interact with each other
        for other_owner in houseowners:
            if other_owner != owner:
                owner.interact_with_other(other_owner)

def run_simulation():
    houseowners = [john, bill, andrew, jane]
    advisors = [breanly]

    simulate_interactions(houseowners, advisors)

    best_system_for_john = john.choose_heating_system(systems)
    best_system_for_bill = bill.choose_heating_system(systems)
    best_system_for_andrew = andrew.choose_heating_system(systems)
    best_system_for_jane = jane.choose_heating_system(systems)
    
    print(f"Best Heating System for {john.name}: {best_system_for_john.name}")
    print(f"Best Heating System for {bill.name}: {best_system_for_bill.name}")
    print(f"Best Heating System for {andrew.name}: {best_system_for_andrew.name}")
    print(f"Best Heating System for {jane.name}: {best_system_for_jane.name}")

if __name__ == "__main__":
    run_simulation()