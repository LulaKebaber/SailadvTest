from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.api.models import system, variable, log
from app.database import Base
from datetime import datetime, timezone


DATABASE_URL = "sqlite:///./data/test.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

systems = [
    {'id': 1, 'name': 'Navigation System'},
    {'id': 2, 'name': 'Generator Main'},
    {'id': 3, 'name': 'Generator Backup'},
    {'id': 4, 'name': 'Battery'},
    {'id': 5, 'name': 'Climate Control'},
]

variables = [
    {'id': 1, 'system_id': 1, 'name': 'latitude', 'type': 'float'},
    {'id': 2, 'system_id': 1, 'name': 'longitude', 'type': 'float'},
    {'id': 3, 'system_id': 1, 'name': 'speed', 'type': 'float'},
    {'id': 4, 'system_id': 1, 'name': 'heading', 'type': 'float'},
    {'id': 5, 'system_id': 2, 'name': 'voltage main', 'type': 'float'},
    {'id': 6, 'system_id': 2, 'name': 'current main', 'type': 'float'},
    {'id': 7, 'system_id': 3, 'name': 'voltage backup', 'type': 'float'},
    {'id': 8, 'system_id': 3, 'name': 'current backup', 'type': 'float'},
    {'id': 9, 'system_id': 2, 'name': 'status backup', 'type': 'string'},
    {'id': 10, 'system_id': 4, 'name': 'battery percent', 'type': 'int'},
    {'id': 11, 'system_id': 5, 'name': 'ac set temperature', 'type': 'float'},
    {'id': 12, 'system_id': 5, 'name': 'ac status', 'type': 'boolean'},
    {'id': 13, 'system_id': 5, 'name': 'current temperature', 'type': 'float'},
]


for system_info in systems:
    system_data = system.System(**system_info)
    db.add(system_data)

for variable_info in variables:
    variable_data = variable.Variable(**variable_info)
    db.add(variable_data)


db.commit()
db.close()
