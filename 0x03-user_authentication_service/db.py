#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User
from typing import Dict


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """saves the user to the database"""
        DBSession = self._session
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            DBSession.add(new_user)
            DBSession.commit()
        except Exception:
            DBSession.rollback()

        return new_user

    def find_user_by(self, **kwa) -> User:
        """find_user_by function"""

        try:
            user = self._session.query(User).filter_by(**kwa).first()
            if user is None:
                raise NoResultFound()
            return user
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()

    def update_user(self, user_id: int, **kwa) -> None:
        """updates a user"""

        user_to_update = self.find_user_by(id=user_id)
        if user_to_update is None:
            return
        for key, value in kwa.items():
            if not hasattr(user_to_update, key):
                raise ValueError
            setattr(user_to_update, key, value)

        self.__session.commit()
