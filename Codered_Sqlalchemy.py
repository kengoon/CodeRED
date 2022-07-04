import sqlite3 
import os
import bcrypt



def create_table():
    conn = sqlite3.connect("Database/user.db")
    cursor = conn.cursor() 


    cursor.execute("CREATE TABLE user_credential (username Text, email Text, password Text)")
    conn.commit()
    conn.close() 

def perform_insert(sql, params):

    if not os.path.exists("Database/user.db"):
        os.mkdir("Database")
        create_table() 
    
    conn = sqlite3.connect("Database/user.db") 
    cursor = conn.cursor() 
    
    cursor.execute(sql, params)
    conn.commit()
    conn.close() 

def perform_select(sql, params):
    conn = sqlite3.connect("Database/user.db") 
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor() 
    cursor.execute(sql, params)
    result = [dict(row) for row in cursor.fetchall()]
    conn.close() 
    return result


def pull_user_credential(email):
    sql = "SELECT password FROM user_credential WHERE email=?"
    params = (email,)
    return perform_select(sql, params)

    

def store_user_credential(username, email, password):

    sql = "INSERT INTO user_credential (username, email, password) VALUES(?,?,?)" 
    password = bcrypt.hashpw(bytes(password, encoding="utf-8"), bcrypt.gensalt())#generate hash
    sql_params = (username, email, password)
    perform_insert(sql, sql_params)

    
