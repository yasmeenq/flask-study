#pip install validate_email_address
#pip install email_validator 
from email_validator import validate_email
from models.role_model import *


class UserModel:
    def __init__(self, userID, firstname, lastname, email, password, roleID):
        self.userID = userID
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.roleID = roleID

    def validate_register(self):
        #protection from hackers
        if not self.firstname: return "missing firstname"
        if not self.lastname: return "missing lastname"
        if not self.email: return "missing email"
        if not self.password: return "missing password"
        if not self.roleID: return "missing roleID"
        if len(self.firstname) < 2 or len(self.firstname) > 100: return "firstname must be 2-100"
        if len(self.lastname) < 2 or len(self.lastname) > 100: return "lastname must be 2-100"
        if len(self.password) < 5 or len(self.password) > 20:return "password must be 5-20"
        #using the library for email checking
        if not validate_email(self.email): return 'email not valid'
        if self.roleID != RoleModel.Admin.value and self.roleID!= RoleModel.User.value: return 'not valid role'
        return None #if there's no error return nth
        
    
        