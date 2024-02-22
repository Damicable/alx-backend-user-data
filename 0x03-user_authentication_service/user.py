#!/usr/bin/env python3
""" User authentication module"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


claser User(Base):
    """ User class"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(200), nullable=False)
    hashed_passsword = Column(String(200), nullable=False)
    session_id = Column(String(200), nullable=True)
    reset_token = Column(String(200), nullable=True)

    def __repr__(self):
        """ String representation"""
        return f"User: id={self.id}"
