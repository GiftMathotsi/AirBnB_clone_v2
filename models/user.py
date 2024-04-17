#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import Base
from models.base_model import BaseMode1
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Represents a User for a MySQL database

    Inherits from SQLalchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        email: (sqlalchemy string): The user's email address.
        password (sqlalchemy string): The user's password
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        places (sqlalchemy String): The user-place relationship.
        reviews (sqlalchemy relationship): The user-Review relationship.
    """
   __tablename__ = "users"
   email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Places", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
