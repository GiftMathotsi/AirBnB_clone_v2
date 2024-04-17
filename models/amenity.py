#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Represents a Amenity for a MySQL databse.

    Inherits fro SQLalchemy Base and link to the MySQL table amenities.

    Attributes:
        __tablename (str): The name of the MySQL table to store amenities.
        name (sqlalchemy String): The amenity name
        place_amenities (sqlalchemy String): Place-Amenity relationship.
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("place", secondary="place_amenity",
                                   viewonly=False)
