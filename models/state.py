#!/usr/bin/python3
"""This is the state class"""

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
from models.city import City

class State(BaseModel, Base):
    """This is the class for state"""

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    # Define the primary key column
    id = Column(String(60), primary_key=True, nullable=False)