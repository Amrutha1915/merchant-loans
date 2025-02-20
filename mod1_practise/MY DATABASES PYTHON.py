import psycopg2
connection =psycopg2.connect(
dbname = "postgres",
user = "postgres",
password = "Saibaba.1915",
host = "localhost", # Change if using a remote server #localhost
port = "5433")
print("Database connection successful!")


def create_table(connection,table_name):
    cursor = connection.cursor
    cursor.excute("""
 CREATE TABLE IF NOT EXISTS employee (
 id SERIAL PRIMARY KEY,
        emp_id int(10) NOT NULL,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL);""")
    connection.commit()
print("tablecreated")

def create_table(connection,table_name):
    cursor = connection.cursor
    cursor.excute("""
 CREATE TABLE IF NOT EXISTS employee (
 id SERIAL PRIMARY KEY,
        emp_id int(10) NOT NULL,
        address VARCHAR(100) NOT NULL,
        mail_id VARCHAR(100) NOT NULL);""")
    connection.commit()
print("tablecreated")