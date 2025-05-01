from db.database import Database

class Mood(object):
    def __init__(self, song: str, feeling: str, description: str = ""):
        self.song = song
        self.feeling = feeling
        self.description = description

    def add_mood(self, db: Database)->None:
        db.query(
            sql_query = f"INSERT INTO {db.moods_log_table_name} (mood, song_title, notes) VALUES (?, ?, ?)",
            params = (self.feeling, self.song, self.description)
        )

    def list_moods(self, db: Database)->list:
        result = db.query(f"SELECT * FROM {db.moods_log_table_name};")
        return result

    def search_moods(self, db: Database, key: str, val: str)->list: 
        result = db.query(f"SELECT * FROM {db.moods_log_table_name} WHERE {key} LIKE '%{val}%';")
        return result

    def __str__(self)->str:
        return f"Feeling {self.feeling} when listening to {self.song}, {('described as: ' + self.description) if len(self.description) else 'with no description'}"
