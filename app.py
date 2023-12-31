from flask import Flask
import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

app = Flask(__name__)

@app.route("/")
def hello_world():
    conn = create_connection("exodus","exodus", None, "localhost", 5432)
    select_company = "SELECT * from company"
    companys = execute_read_query(conn, select_company)
    for company in companys:
        print(type(company))
    return f"<p>Hello, World! {companys}</p>"