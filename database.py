import const
import os.path as p
import sqlite3 as sql

"""
create database if not exists
create tables if not exists
make a class to access connection globally
"""

class Database(object):
    def __init__(self):
        self.create_db()

    def create_db(self)->None:
        self.connection = sql.connect(const.get_db_file_name())
        self.cursor = self.connection.cursor()
        if not self.tables_exist():
            try:
                self.create_tables()
                self.connection.commit()
            except Exception as e:
                self.connection.rollback()
                print("Couldn't create tables, rollbacked")
                print(e)


    # helper method
    def query(self, sql_query: str, autocommit=True)->list:
        self.cursor.execute(sql_query)
        if autocommit:
            self.connection.commit()
        return self.cursor.fetchall()

    def tables_exist(self)->bool:
        result = self.query(self.get_show_tables_query())
        self.tables_exist = len(result) > 0
        return self.tables_exist

    def get_show_tables_query(self)->str: 
        return """
        SELECT name
        FROM sqlite_schema
        WHERE type = 'table'
        AND name NOT LIKE 'sqlite_%';
        """
    
    def create_tables(self)->None:
        self.create_user_table()
        self.create_moods_log_table()
    
    def create_user_table(self)->None:
        self.query(self.get_create_user_table_query(), False)

    def create_moods_log_table(self)->None:
        self.query(self.get_create_moods_log_table_query(), False)
    
    def get_create_user_table_query(self)->str:
        return """
            CREATE TABLE user (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """

    def get_create_moods_log_table_query(self)->str:
        return """
            CREATE TABLE moods_log (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                mood TEXT NOT NULL,
                song_title TEXT NOT NULL,
                notes TEXT,
                created_at TIMESTAMP NOT NULL DEFAULT CURERNT_TIMESTAMP
            );
        """


def __main__():
    db = Database()

__main__()