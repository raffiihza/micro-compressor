# This file is intended for checking database connections only

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL_2 = os.getenv('DATABASE_URL_2')

try:
    conn = psycopg2.connect(DATABASE_URL)
    conn.close()
    print("1st database is okay")
except Exception as e:
    print("Error:", e)
    print("1st database is error")

try:
    conn = psycopg2.connect(DATABASE_URL_2)
    conn.close()
    print("1st database is okay")
except Exception as e:
    print("Error:", e)
    print("1st database is error")