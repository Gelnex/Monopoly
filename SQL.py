def connectionDB(table):

    import mysql.connector

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="monopolyCDP"
    )


    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")

    result = cur.fetchall()

    cur.close()
    conn.close()
    
    return result

if __name__ == "__main__":
    print(connectionDB("cases"))