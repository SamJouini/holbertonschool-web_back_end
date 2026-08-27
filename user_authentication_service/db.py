#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

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
        """Adds a new user to the database.

        Args:
            email (str): The email address of the user.
            hashed_password (str): The already-hashed password of the user.

        Returns:
            User: The newly created User object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Finds the first user matching the given filter arguments.

        Args:
            **kwargs: Arbitrary keyword arguments corresponding to User
                column names and their expected values.

        Returns:
            User: The first User object matching the filter.

        Raises:
            NoResultFound: If no user matches the given filter.
            InvalidRequestError: If invalid query arguments are passed.
        """
        return self._session.query(User).filter_by(**kwargs).one()

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user's attributes and commits the change.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: Arbitrary keyword arguments corresponding to User
                column names and their new values.

        Returns:
            None

        Raises:
            ValueError: If an argument does not correspond to a
                valid user attribute.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(
                    "{} is not a valid user attribute".format(key))
            setattr(user, key, value)
        self._session.commit()
