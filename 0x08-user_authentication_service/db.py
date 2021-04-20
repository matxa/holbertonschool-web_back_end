#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


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
        """ Add User to DB
        """
        new_user = User()
        new_user.email = email
        new_user.hashed_password = hashed_password

        session = self._session
        session.add(new_user)
        session.commit()

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Find User using kwargs
        """
        session = self._session
        user = User()
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise InvalidRequestError
            query = "User.{} == '{}'".format(key, value)
            user_result = session.query(User).filter(eval(query)).first()
            if user_result is None:
                raise NoResultFound
            return user_result

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user using kwargs
        Parameters
        ----------
        kwargs
            key word arguments
        Return
        ------
            None
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
        return None
