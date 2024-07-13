import mysql.connector

class DAL:
    #constructor 
    def __init__(self):
        self.connection = mysql.connector.connect(
        host="localhost",
        user="root", password="1234", 
        database="classicmodels") # localhost = current machine.

    def get_table(self, sql, params=None):
        with  self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
            return table 
    
    # def get_table_v1(self, sql, params=None):
    #     self.cursor = self.connection.cursor()
    #     self.cursor.execute(sql, params)
    #     table = self.cursor.fetchall()
    #     self.cursor.close()
    #     return table 

    def get_scalar(self, sql, params=None):
        with  self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchone()
            return table 
    
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            last_row_id = cursor.lastrowid
            return last_row_id

    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
            return row_count

    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
            return row_count

    def close(self):
        self.connection.close() 