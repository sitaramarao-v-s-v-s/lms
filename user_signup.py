"""This module is creates the user and updates in the database.
"""
import base64
import valid
from connection import cursor , mydb

def user_signup():
    """This module is used for user Signup
    """
    try:
        # Signup User Input
        uid = valid.userid(input('enter user id : ').strip().lower())
        user_name = valid.user_name_validation(input('enter user name : ').strip())
        user_mail = valid.email_validation(input('enter user mail : ').strip().lower())
        password =  valid.password_validation(input('enter password : ').strip())
        query = "select mail_id from user where user_id =%s or mail_id =%s;"
        if cursor.execute(query, (uid,user_mail)):
            print('user already exists')
        else:
            encoded_pwd = base64.b64encode(password.encode('ascii'))
            query = "insert into user (user_id,user_name,mail_id,password) values(%s,%s,%s,%s)"
            cursor.execute(query,(uid,user_name, user_mail, encoded_pwd))
            mydb.commit()
            print("User Creation Successful")
    except Exception as exception_e:
        print("Error",exception_e)
  