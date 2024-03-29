#!/usr/bin/python3
""" python file that contains the class definition of a
State and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """
    class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a
    string with maximum 128 characters and can’t be null
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
