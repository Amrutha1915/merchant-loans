def create_transaction(connection, member_id, amount, description, transaction_type = "withdrawal"):
    cursor = connection.cursor()
    cursor.execute(f"""
    INSERT INTO fi_member_transactions (member_id, amount, transaction_type, description)
    VALUES (%s, %s, %s, %s) RETURNING transaction_id ;
    """, (member_id, amount, transaction_type, description))
    connection.commit()
    id = cursor.fetchone()[0]
    print(f"Record inserted successfully!: {id}")
    return id