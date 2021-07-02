import cx_Oracle

HOST = "DESKTOP-TNPL4M2.mshome.net"
PORT = "1521"
SERVICE_NAME = "XEPDB1"
USER = "cse"
PASS = "cse"


def store_passwords(password, user_email, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        query = """insert into accounts(password, email, username, url, app_name) values ('{}','{}','{}','{}','{}')""".format(
            password, user_email, username, url, app_name
        )
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print(e)


def connect():
    try:
        dsn_tns = cx_Oracle.makedsn(HOST, PORT, service_name=SERVICE_NAME)
        conn = cx_Oracle.connect(user=USER, password=PASS, dsn=dsn_tns)
        return conn
    except Exception as e:
        print(e)


def find_password(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        query = """ SELECT password FROM accounts WHERE app_name = '""" + app_name + "'"
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchone()
        print("Password is: ")
        print(result[0])
    except Exception as e:
        print(e)


def find_users(user_email):
    data = ("Password: ", "Email: ", "Username: ", "url: ", "App/Site name: ")
    try:
        connection = connect()
        cursor = connection.cursor()
        query = """ SELECT * FROM accounts WHERE email = '""" + user_email + "'"
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()
        print("")
        print("RESULT")
        print("")
        for row in result:
            for i in range(len(row) - 1):
                print(data[i] + row[i])
        print("")
        print("-" * 30)
    except Exception as e:
        print(e)
