import sqlite3
from email.message import EmailMessage
import ssl
import smtplib

class UserDetails:
    __db_connection = None
    __db_cursor = None
    
    def __init__(self):
        self.__db_connection = sqlite3.connect('server.sqlite')
        self.__db_cursor = self.__db_connection.cursor()

        query = '''
            CREATE TABLE IF NOT EXISTS Users (
                UID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR2(150) NOT NULL,
                Email VARCHAR2(150) NOT NULL UNIQUE
            );
        '''

        self.__db_cursor.execute(query)

    def insert_row(self, name, email):
        query = '''
            INSERT INTO Users(Name, Email)
            VALUES (?, ?)        
        '''

        self.__db_cursor.execute(query, (name, email))

        self.__db_connection.commit()
        email_sender = 'nitcevents12@gmail.com'
        email_password = 'oxigjruoqjeevenu'
        email_receiver = email

        subject = 'FINALLY'

        body = """
        Aa gya kya!!!
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver, em.as_string())

    def retrieve_row(self):
        query = '''
            SELECT * FROM Users
        '''

        self.__db_cursor.execute(query)


def main():
    user = UserDetails()
    # name = input('Enter Name: ')
    # email = input('Enter email: ')

    # user.insert_row(name,email)

    user.retrieve_row()


if __name__ == '__main__':
    main()