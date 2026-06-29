"""
Module: User Management
Description: This module provides functionality for managing user accounts.

Author: John Doe <johndoe@example.com>
Version: 1.0.0
"""

class User:
    """
    Class representing a user account.

    Attributes:
        id (int): The unique identifier of the user.
        username (str): The username associated with the account.
        email (str): The email address of the user.
    """

    def __init__(self, id: int, username: str, email: str):
        """
        Initialize a User object.

        Args:
            id (int): The unique identifier of the user.
            username (str): The username associated with the account.
            email (str): The email address of the user.
        """
        self.id = id
        self.username = username
        self.email = email

    def get_id(self) -> int:
        """
        Return the user's unique identifier.
        """
        return self.id

    def get_username(self) -> str:
        """
        Return the user's username.
        """
        return self.username

    def get_email(self) -> str:
        """
        Return the user's email address.
        """
        return self.email


# Usage Example
user = User(1, "johndoe", "johndoe@example.com")

user_id = user.get_id()
print(f"User ID: {user_id}")