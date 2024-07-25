from utils.dal import DAL 

class AuthLogic:
    def __init__(self):
        self.dal = DAL()

    def add_user(self, user):
        sql = "INSERT INTO usersflask(firstname, lastname, password, email, roleID) VAlUES(%s,%s,%s,%s,%s)"
        self.dal.insert(sql, (user.firstname, user.lastname, user.password, user.email, user.roleID))

    def is_email_taken(self, email):
        sql = "SELECT EXISTS(SELECT * FROM usersflask WHERE email = %s) as is_taken" #this returns true or false if taken/ is_taken is a variable name
        result = self.dal.get_scalar(sql, (email,))
        return result['is_taken'] == 1 #if 1 true if 0 false

    def close(self):
        self.dal.close()
