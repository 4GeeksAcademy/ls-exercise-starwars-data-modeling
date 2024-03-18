import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites = Column(Integer,(ForeignKey("favorites.id")))

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,(ForeignKey("user.id")))
    char_id_liked = Column(Integer,(ForeignKey("characters.id")))
    plan_id_liked = Column(Integer,(ForeignKey("planets.id")))
    
    

    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(Integer,(ForeignKey("planets.id")))
    
    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period= Column(String(250))
    orbital_period= Column(String(250))
    diameter= Column(String(250))
    climate= Column(String(250))
    gravity= Column(String(250))
    terrain= Column(String(250))
    surface_water = Column(String(250))
    population = Column(String(250))
    residents= Column(Integer,(ForeignKey("characters.id")))

    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')