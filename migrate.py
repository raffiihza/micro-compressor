# This file is intended for migrating database tables

import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL_2 = os.getenv('DATABASE_URL_2')

def create_table_image(conn):
    """Create a table named 'history'."""
    cursor = conn.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS history (
            id SERIAL PRIMARY KEY,
            prompt TEXT,
            image BYTEA
        )
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()

def create_table_text(conn):
    """Create a table named 'history'."""
    cursor = conn.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS history (
            id SERIAL PRIMARY KEY,
            prompt TEXT,
            text TEXT
        )
    """
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()

def show_history_table_contents(conn):
    """Fetch and print the contents of the 'history' table."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    rows = cursor.fetchall()
    print("History Table:")
    for row in rows:
        print(row)
    cursor.close()

def show_history_table_columns(conn):
    """Fetch and print the contents of the 'history' table."""
    cursor = conn.cursor()
    
    # Fetch column names
    cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'history'")
    columns = [row[0] for row in cursor.fetchall()]
    print("Columns:", columns)
    
    # Fetch and print rows
    cursor.execute("SELECT * FROM history")
    rows = cursor.fetchall()
    print("History Table:")
    for row in rows:
        print(row)
    cursor.close()

def main():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(DATABASE_URL)

        # Create the 'history' table
        create_table_image(conn)

        print("Table 'history' created successfully for the 1st database!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(DATABASE_URL_2)

        # Create the 'history' table
        create_table_text(conn)

        print("Table 'history' created successfully for the 2nd database!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
