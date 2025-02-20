
import psycopg2

import configparser
import configparser
# Initialize the config parser
config = configparser.ConfigParser()
config.read('credentials.cfg')


connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Saibaba.1915",
        host="localhost",
        port="5433"
)
 
try:
 connection = psycopg2.connect(
          dbname= config['postgres'] ["postgres"],
          user=config["postgres"],
          password=config["Saibaba.1915"],
          host=config["localhost"],
          port=config["5433"]
        
        )
 
 print("Database connection successful!")
 print("Database connection successful!")

except Exception as e:

 print("Error connecting to the database:", e)


 cursor = connection.cursor()
query="select * from accounts;"
cursor.execute("SELECT * from accounts;")

print()

cursor.close()
connection.close()
