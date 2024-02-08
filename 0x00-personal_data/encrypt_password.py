#!/usr/bin/env python3
""" Encrypting passwords module"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Salted pass generation function"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    is_valid - Function that checks for validity using boolean
    @hashed_password: bytes type
    @password: String type password
    Return: Boolean
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
