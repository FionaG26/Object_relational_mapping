# models/create_tables.py
from models import Base, engine

# Create tables
Base.metadata.create_all(engine)
