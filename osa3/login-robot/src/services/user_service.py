from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        # käyttäjätunnuksen tulee koostua kirjaimista a-z
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username is not valid")
        # käyttäjänimen täytyy olla vähintään kolme merkkiä pitkä
        if len(username) < 3:
            raise UserInputError("Username is too short")
        # käyttäjänimi ei saa olla jo käytössä
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username is already taken") 
        # salasanan täytyy olla vähintään 8 merkkiä pitkä
        if len(password) < 8:
            raise UserInputError("Password is too short")
        # salasana ei saa koostua pelkästään kirjaimista
        if re.match("^[a-z]+$", password):
            raise UserInputError("Password must include characters another than letters")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
