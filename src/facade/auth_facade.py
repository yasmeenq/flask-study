from logic.auth_logic import AuthLogic
from flask import request, session #we can save things on the session temporarily 
from models.user_model import UserModel
from models.role_model import RoleModel
from models.client_error import *
from models.credentials_model import *
from utils.cyber import *

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
        if error: raise ValidationError('register error..', user) #why is it important to send the object user? so it wont delete all the info from the form every time
        if self.logic.is_email_taken(email): raise ValidationError('email already exists', user)
        #before you add user convert the password to hash sh512 code
        user.password = Cyber.hash(user.password)
        
        self.logic.add_user(user)


    def login(self):
        email = request.form.get('email')
        password = request.form.get('password')
        credentials = CredentialModel(email, Cyber.hash(password)) #reconvert the password to normal text
        error = credentials.validate_login()
        if error: raise ValidationError(error, credentials)
        
        user = self.logic.get_user(credentials)
        if not user: raise AuthError("Incorrect email or password", credentials) #pass credentials so it saves email and password incase of error so it wont be deleted everytime
        #Assaf used  AuthError("Incorrect email or password", user) but i see that this is more accurate
        
        del user['password'] #delete from session dictionary password key
        session["current_user"] = user  #save user in the session


    def logout(self):
        session.clear()  #delete everything you saved temporarily, any saved things are now saved to the database.

    #block guests - view only 
    def block_anonymous(self): 
        user = session.get("current_user")
        if not user: raise AuthError("you are not logged in")

    #block non admin 
    def block_non_admin(self):
        user = session.get("current_user")
        if not user: raise AuthError("you are not logged in")
        if user["roleID"] != RoleModel.Admin.value: raise AuthError("you are not allowed")
        
    #block non user
    def block_non_user(self):
        user = session.get("current_user")
        if not user: raise AuthError("you are not logged in")
        if user["roleID"] != RoleModel.User.value: raise AuthError("you are not allowed")        


    def close(self):
        self.logic.close()