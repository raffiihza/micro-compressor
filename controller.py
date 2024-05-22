import psycopg2

def get(db):
    try:
        conn = psycopg2.connect(db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM history")
        history_data = cursor.fetchall()
        cursor.close()
        conn.close()
        return history_data
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL:", error)
        return []

def store_image(db, prompt, image):
    try:
        conn = psycopg2.connect(db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (prompt, image) VALUES (%s, %s)", (prompt, image))
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while adding data to PostgreSQL:", error)

def store_text(db, prompt, text):
    try:
        conn = psycopg2.connect(db)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (prompt, text) VALUES (%s, %s)", (prompt, text))
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while adding data to PostgreSQL:", error)

def reset(db):
    try:
        conn = psycopg2.connect(db)
        cursor = conn.cursor()
        
        delete_data_query = "DELETE FROM history"
        cursor.execute(delete_data_query)
        conn.commit()
        print("All data from 'history' table has been deleted.")
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")