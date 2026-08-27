#!/usr/bin/env python3
"""Auth module
"""
from uuid import uuid4
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password with a randomly-generated salt.
    Args:
        password (str): The plain-text password to hash.
    Returns:
        bytes: The salted hash of the input password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a new unique identifier.
    Returns:
        str: The string representation of a newly generated UUID.
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializes a new Auth instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user in the database.
        Args:
            email (str): The email address of the new user.
            password (str): The plain-text password of the new user.
        Returns:
            User: The newly created User object.
        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a user's login credentials.
        Args:
            email (str): The email address of the user.
            password (str): The plain-text password to check.
        Returns:
            bool: True if the email/password combination is valid,
                False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(
            password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """Creates a new session for a user.
        Args:
            email (str): The email address of the user.
        Returns:
            str: The newly generated session ID, or None if no user
                is found for the given email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """Retrieves a user based on a session ID.
        Args:
            session_id (str): The session ID to look up.
        Returns:
            User: The corresponding User object, or None if the
                session ID is None or no user is found.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """Destroys a user's session by clearing their session ID.
        Args:
            user_id (int): The ID of the user whose session should
                be destroyed.
        Returns:
            None
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generates a password reset token for a user.
        Args:
            email (str): The email address of the user requesting
                a password reset.
        Returns:
            str: The newly generated reset token.
        Raises:
            ValueError: If no user is found for the given email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError(
                "No user found with email {}".format(email))
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates a user's password using a reset token.
        Args:
            reset_token (str): The reset token identifying the user.
            password (str): The new plain-text password to set.
        Returns:
            None
        Raises:
            ValueError: If no user is found for the given reset token.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError("Invalid reset token")
        hashed_password = _hash_password(password)
        self._db.update_user(
            user.id,
            hashed_password=hashed_password,
            reset_token=None)
