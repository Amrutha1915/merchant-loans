import psycopg2



# database Details
connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Saibaba.1915",
        host="localhost",
        port="5433"
    
)

# Establishing the Connection
try:
  connection=psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Saibaba.1915",
        host="localhost",
        port="5433"
    
)

  print("db connected created successfully!")
except Exception as e: 

  print("error in connection")


  


  # Creating a cursor to execute the query
  #creating a table


def create_table(connection,table_name):
 cursor = connection.cursor()
 if(table_name  == 'employee'):
          cursor.execute(""" 
            create table if not exist employee(
              id serial primary key ,
              name varchar(30) Not Null ,
              gender varchar(10) Not Null); 
     """)
   
connection.commit()
print("table created successfully")




