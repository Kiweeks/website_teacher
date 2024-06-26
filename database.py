import psycopg2
from psycopg2.extras import RealDictCursor
from os import getenv
from dotenv import load_dotenv

load_dotenv()


db = psycopg2.connect(
    database=getenv('DB_NAME'),
    user=getenv('DB_USER'),
    password=getenv('DB_PASS'),
    host=getenv('DB_HOST')
)

db.autocommit = True

cursor = db.cursor(cursor_factory=RealDictCursor)