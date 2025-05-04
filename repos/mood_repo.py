from db.database import Database
from models.mood import Mood

class MoodRepository:
    db = None
    
    def __init__(self, db: Database):
        self.db = db

    def add(self, mood: Mood)->None:
        sql = f"INSERT INTO {self.db.moods_log_table_name} (mood, song_title, notes) VALUES (?, ?, ?)"
        params = (mood.feeling, mood.song, mood.description)
        self.db.query(sql,params)

    def all(self, columns: str = None)->list[Mood]:
        sql = f"SELECT * FROM {self.db.moods_log_table_name};" if not columns else f"SELECT {columns} FROM {self.db.moods_log_table_name};"
        result = self.db.query()
        return result

    def search(self, key: str, val: str)->list[Mood]: 
        sql = f"SELECT * FROM {self.db.moods_log_table_name} WHERE {key} LIKE ?;"
        params = (f"%{val}%",)
        result = self.db.query(sql, params)
        return result
    
    def multi_search(self, keys: list[str], values: list[str], operators: list[str] = None)->list[Mood]:
        if not operators:
            op = 'LIKE'
        sql = f"SELECT * FROM {self.db.moods_log_table_name} WHERE "
        statements = []
        for i in range(len(keys)):
            op = op if not operators else operators[i]
            statements.append(f"{keys[i]} {op} ? ")
            values[i] = f"%{values[i]}%" if op == "LIKE" else values[i]
        sql += " AND ".join(statements)
        result = self.db.query(sql, tuple(values))
        return result

    def truncate(self)->None:
        sql = f"DELETE FROM {self.db.moods_log_table_name};"
