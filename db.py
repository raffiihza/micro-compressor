import os

# Put your postgres database URIs here or on environment variables

DB_URL = "postgres://"
DB_URL_2 = "postgres://"

DATABASE_URL = os.environ.get('DB_URL', DB_URL) 
DATABASE_URL_2 = os.environ.get('DB_URL_2', DB_URL_2)