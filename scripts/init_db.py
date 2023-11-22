import sys
import os
import requests


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


systems_data = [
    {'name': 'Navigation System'},
    {'name': 'Generator Main'},
    {'name': 'Generator Backup'},
    {'name': 'Battery'},
    {'name': 'Climate Control'},
]

variables_data = [
    {'system_id': 1, 'name': 'latitude', 'type': 'float'},
    {'system_id': 1, 'name': 'longitude', 'type': 'float'},
    {'system_id': 1, 'name': 'speed', 'type': 'float'},
    {'system_id': 1, 'name': 'heading', 'type': 'float'},
    {'system_id': 2, 'name': 'voltage main', 'type': 'float'},
    {'system_id': 2, 'name': 'current main', 'type': 'float'},
    {'system_id': 3, 'name': 'voltage backup', 'type': 'float'},
    {'system_id': 3, 'name': 'current backup', 'type': 'float'},
    {'system_id': 2, 'name': 'status backup', 'type': 'string'},
    {'system_id': 4, 'name': 'battery percent', 'type': 'int'},
    {'system_id': 5, 'name': 'ac set temperature', 'type': 'float'},
    {'system_id': 5, 'name': 'ac status', 'type': 'boolean'},
    {'system_id': 5, 'name': 'current temperature', 'type': 'float'},
]

for system_data in systems_data:
    response = requests.post("http://0.0.0.0:8000/api/system", json=system_data)

for variable_data in variables_data:
    response = requests.post("http://0.0.0.0:8000/api/variable", json=variable_data)