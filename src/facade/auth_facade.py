from logic.auth_logic import AuthLogic
from flask import request
from models.user_model import UserModel
from models.role_model import RoleModel
from models.client_error import *

class AuthFacade:
    def __init__(self):
        self.logic = AuthLogic()

    def register(self):
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get('email')
        password = request.form.get('password')
        user = UserModel(None, firstname, lastname, email, password, RoleModel.User.value)
        error = user.validate_register()
        if error: raise ValueError('register error..')
        if self.logic.is_email_taken(email): raise ValidationError('email already exists')
        self.logic.add_user(user)


    def close(self):
        self.logic.close()