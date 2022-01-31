#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.base import attribute_str
import sqlalchemy
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='states')
    else:
        @property
        def cities(self):
            """ getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            from models import storage
            from models.city import City
            list = []
            cities = storage.all(City)
            for value in cities.values():
                if value.state_id == self.id:
                    list.append(value)
            return list
