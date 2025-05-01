import db.const as const
import sqlite3 as sql

"""
create database if not exists
create tables if not exists
make a class to access connection globally
"""

class Database(object):
    moods_log_table_name = 'moods_log'
    user_table_name = 'user'

    def __init__(self):
        self.db_name = const.get_db_file_name()
        self.create_db()

    def create_db(self)->None:
        self.connection = sql.connect(self.db_name)
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
    def query(self, sql_query: str, params: tuple = (), autocommit: bool = True)->list:
        self.cursor.execute(sql_query, params)
        if autocommit:
            self.connection.commit()
        return self.cursor.fetchall()

    def tables_exist(self)->bool:
        result = self.query(self.get_show_tables_query())
        self.is_exist = len(result) > 0
        return self.is_exist

    def get_num_tables(self)->int:
        return len(self.query(self.get_show_tables_query()))

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
        self.query(self.get_create_user_table_query(), autocommit=False)

    def create_moods_log_table(self)->None:
        self.query(self.get_create_moods_log_table_query(), autocommit=False)
    
    def get_create_user_table_query(self)->str:
        return f"""
            CREATE TABLE {self.user_table_name} (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """

    def get_create_moods_log_table_query(self)->str:
        return f"""
            CREATE TABLE {self.moods_log_table_name} (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                mood TEXT NOT NULL,
                song_title TEXT NOT NULL,
                notes TEXT,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """
    
    def __str__(self)->str:
        return f"Database connection to: {self.db_name}, having {self.get_num_tables()} tables"
