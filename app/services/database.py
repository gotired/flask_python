import os

from dotenv import load_dotenv
from psycopg2 import connect as psycopg2_connect
from pymongo import MongoClient

load_dotenv()


class MongoDB:
    """MongoDB Connect Module"""

    @staticmethod
    async def connect():
        """Connect to MongoDB"""
        cluster_url = os.getenv("DATABASE_URL")
        client = MongoClient(cluster_url)
        database_name = os.getenv("DATABASE_NAME") 
        return client[database_name]

    async def collection(self, collection_name: str):
        """Select Database Collection"""
        database = await self.connect()
        return database[collection_name]


class PostgreSQL:
    """PostgreSQL Connect Module"""

    @staticmethod
    async def connect():
        """Connect to PostgreSQL"""
        connection_string = os.getenv("DATABASE_URL")
        conn = psycopg2_connect(connection_string)
        return conn

    async def get_cursor(self):
        """Get a cursor from the PostgreSQL connection"""
        conn = await self.connect()
        return conn.cursor()

    async def close_connection(self):
        """Close the PostgreSQL connection"""
        conn = await self.connect()
        conn.close()
