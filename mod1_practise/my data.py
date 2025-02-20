import psycopg2
connection =psycopg2.connect(
dbname = "postgres",
user = "mydatabase",
password = "Saibaba.1915",
host = "localhost", # Change if using a remote server #localhost
port = "5433")
print("Database connection successful!")

def create_table(connection,table_name):
    cursor = connection.cursor
    cursor.excute("""
 CREATE TABLE IF NOT EXISTS acc (
 id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
          gender VARCHAR(15) );""")
    connection.commit()
print("tablecreated")

def create_member(connection, name, age, membership_type):
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO account (name, age, membership_type)
VALUES (%s, %s, %s);
""", ("Alice", 30, "Premium"),
      ("Robert", 31, "gold"),
      ("Alex", 32, "silver"))
    connection.commit()
print("updated")
