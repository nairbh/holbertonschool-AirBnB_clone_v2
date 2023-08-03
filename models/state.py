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
    cities = relationship('City', cascade='all, delete',
                          backref='state')

    @property
    def cities(self):
        """Returns the list of City instances with
           state_id equals to the current State.id"""

        city_list = []
        city_dict = storage.all(City)

        for city in city_dict.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
