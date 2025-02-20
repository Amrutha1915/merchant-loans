class Transcation:
    #class variable
 number_of_transcation = 0

import psycopg2

def __init__(sb, aid, mid, amount, type, id):
        #instance variable
        sb.address_id = aid
        sb.member_id = mid
        sb.amount = amount
        sb.type = type
        sb.id = id

        connection = psycopg2.connect(
        dbname="postgres",
        dbuser="postgres",
        password="Saibaba.1915",
        host="localhost",
        port="5433"
        )
print('table created sucessfully')


# create_transcation
def create_transcation(sb):
      cursor=connection.cursor()
      cursor.execute("""insert into transcations(transcation_id, transcation_date, amount, type, branch_id)
    #values(?,?,?,?)""", )(sb.transcation_id, sb.transcation_date, sb.amount, sb.type, sb.branch_id)
      cursor.commit()
print('done')

#retrive transcation
def retrive_Transcation(sd):
 cursor=connection.cursor()
 cursor.execute(""" select * from transcation where transcation_id = ?
""",(sb.transcation_id,))
 cursor.commit()
print('done')