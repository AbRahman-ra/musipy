from db.database import Database
from models.mood import Mood

class MoodRepository:
    db = None
    num_required_fields = 2
    
    def __init__(self, db: Database):
        self.db = db

    def add(self, mood: Mood)->None:
        sql = f"INSERT INTO {self.db.moods_log_table_name} (mood, song_title, notes) VALUES (?, ?, ?)"
        params = (mood.feeling, mood.song, mood.description)
        self.db.query(sql,params)
        mood.id = self.db.query("SELECT last_insert_rowid()")[0][0]

    def all(self, columns: str = None)->list[Mood]:
        sql = f"SELECT * FROM {self.db.moods_log_table_name};" if not columns else f"SELECT {columns} FROM {self.db.moods_log_table_name};"
        result = [Mood.from_record(record) for record in self.db.query(sql)]
        return result

    def last(self, columns: str = None)->Mood|None:
        sql = f"SELECT {'*' if not columns else columns} FROM {self.db.moods_log_table_name} ORDER BY id DESC LIMIT 1;"
        result = self.db.query(sql)
        return Mood.from_record(result[0]) if len(result) else None

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
        self.db.query(sql)

    def last_mood(self)->Mood|None:
        sql = f"SELECT * FROM {self.db.moods_log_table_name} ORDER BY created_at DESC LIMIT 1"
        result = self.db.query(sql)
        return result[0] if len(result) else None
