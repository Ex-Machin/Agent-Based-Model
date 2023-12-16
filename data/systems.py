from models.HeatingSystem import HeatingSystem
import json

with open('data/systems.json', 'r') as file:
    systems_data = json.load(file)

systems = [HeatingSystem(**data) for data in systems_data]