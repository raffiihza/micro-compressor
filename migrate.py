import psycopg2
from psycopg2 import sql
from db import DB_URL

def create_table(conn):
    """Create a table named 'history'."""
    cursor = conn.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS history (
            id SERIAL PRIMARY KEY,
            prompt TEXT,
            text TEXT,
            image BYTEA
        )
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()

def main():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(POSTGRES_URI)

        # Create the 'history' table
        create_table(conn)

        print("Table 'history' created successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
