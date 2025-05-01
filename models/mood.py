from db.database import Database
from dataclasses import dataclass

# mood object
@dataclass
class Mood:
    song: str
    feeling: str
    description: str = ""

    def __str__(self)->str:
        return f"Feeling {self.feeling} when listening to {self.song}, {('described as: ' + self.description) if len(self.description) else 'with no description'}"

# Moods container
class MoodRepository:
    db = None
    
    def __init__(self, db: Database):
        self.db = db

    def add(self, mood: Mood)->None:
        sql = f"INSERT INTO {self.db.moods_log_table_name} (mood, song_title, notes) VALUES (?, ?, ?)"
        params = (mood.feeling, mood.song, mood.description)
        self.db.query(sql,params)

    def all(self)->list[Mood]:
        result = self.db.query(f"SELECT * FROM {self.db.moods_log_table_name};")
        return result

    def search(self, key: str, val: str)->list[Mood]: 
        sql = f"SELECT * FROM {self.db.moods_log_table_name} WHERE {key} LIKE ?;"
        params = (f"%{val}%",)
        result = self.db.query(sql, params)
        return result
