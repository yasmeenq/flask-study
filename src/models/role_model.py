from enum import Enum
#enum is like dictionary: a name and a value

class RoleModel(Enum):
    Admin = 1 
    User = 2    
    
#print(RoleModel.Admin.value)  #1
#print(RoleModel.User.name)  #Admin

