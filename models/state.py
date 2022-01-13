#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv

import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', cascade="all, delete-orphan", backref='state')

    else:
        name = ''

        @property
        def cities(self):
            """getter attribute cities that returns the list of City 
            instances with state_id"""
            from models import storage

            new_list = []
            for city_id, city, in storage.all(City).items():
                if city.state_id == self.id:
                    new_list.appent(city)
            return new_list
