# ============================================================================#
# = IMPORTS DES BIBLIOTHEQUES ET DES CLASSES                                 =#
# ============================================================================#
import mysql.connector

"""
    Qui : Engles Felix
    Quand : 07/04/2024
    Quoi : Importation de la Base De Données MYSQL 
"""

def connectionDB(table):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="monopolyCDP"
        )

        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        result = cur.fetchall()

    except mysql.connector.Error as err:
        print("Error accessing the database:", err)
        result = None

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
    
    return result

if __name__ == "__main__":
    print(connectionDB("cases"))