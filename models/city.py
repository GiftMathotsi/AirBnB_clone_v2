#!/usr/bin/python3
"""Defines the city class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Represents a city from MySQL database.

    Inherits from SQLALCHEMY Base and links to the MYSQL table cities.

    Attributes:
        __tablename__ (str): The name of the MYSQL table to store Cities.
        name (sqlalchemy String): The name of the city.
        state_id (sqlalchemy String): The state id of the city.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
