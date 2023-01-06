#!/usr/bin/python3
<<<<<<< HEAD

""" State Module for HBNB project """

from models.base_model import BaseModel, Base

from models import storage_type

from sqlalchemy import Column, String





class Amenity(BaseModel, Base):

    '''amenity class'''

    __tablename__ = 'amenities'

    if storage_type == 'db':

        name = Column(String(128), nullable=False)

    else:

=======
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
>>>>>>> 11f920e69a43f50dce1b1e0bb06e817c3bfa2e13
        name = ""
