import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    name = Column(String(250))
    lastname = Column(String())
    origin_planet = Column(String())
    favorite = relationship('Favorite')

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

# class Ship
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    ship_id = Column(Integer, ForeignKey('ship.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    ship = relationship('Ship')
    planet = relationship('Planet')
    character = relationship('Character')

class Ship(Base):
    __tablename__ = 'ship'
    id = Column(Integer, primary_key = True)
    model = Column(String(400), nullable = False)
    wheigth = Column(String(400), nullable = False)
    hp = Column(Integer, nullable = False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(400), nullable = False)
    habitats = Column(String(400), nullable = False)
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key = True)
    fullname = Column(String(400), nullable = False)
    occupation = Column(String(400), nullable = False)
    powers = Column(Boolean, nullable = False)
    origin_planet = Column(String(400), nullable = False)
    age = Column(String(400), nullable = False)
    heigth = Column(String(400), nullable = False)
    wheigth = Column(String(400), nullable = False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
