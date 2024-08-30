from datetime import datetime
from flask import session

class Logger: #to handle errors
    #path to log file 
    __log_file = './logger.log'

    @staticmethod
    def log(message):
        now = datetime.now()
        #open a file
        with open(Logger.__log_file, "a") as file: #append to file
            file.write(str(now) + '\n')
            file.write(message + '\n')
            
            #write user data if exists
            user = session.get('current_user')
            if user:
                file.write('userID: ' + str(user['userID']) + 'user email: ' + user['email'] + '\n')
                file.write('=============================================================' + '\n')
