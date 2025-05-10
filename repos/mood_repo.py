from db.database import Database
from models.mood import Mood
from typing import List

class MoodRepository:
    db = None
    num_required_fields = 2
    cli_columns = ['song', 'feeling', 'mood', 'details', 'notes', 'id']
    cli_db_mapper = {
        "id": "id",
        "song": "song_title",
        "feeling": "mood",
        "mood": "mood",
        "details": "notes",
        "notes": "notes",
    }

    cli_mood_mapper = {
        "id": "id",
        "song": "song",
        "feeling": "feeling",
        "mood": "feeling",
        "details": "description",
        "notes": "description",
    }
    
    def __init__(self, db: Database):
        self.db = db

    def create_mood_from_cli(self, data: dict)->Mood:
        new_data = {}
        for cli_column, field in data.items():
            mood_property = self.cli_mood_mapper[cli_column]
            new_data[mood_property] = field
        return Mood(new_data["song"], new_data["feeling"], new_data.get("description") if new_data.get("description") else "")

    def add(self, mood: Mood)->None:
        sql = f"INSERT INTO {self.db.moods_log_table_name} (mood, song_title, notes) VALUES (?, ?, ?)"
        params = (mood.feeling, mood.song, mood.description)
        self.db.query(sql,params)
        mood.id = self.db.query("SELECT last_insert_rowid()")[0][0]

    def all(self, columns: str = None)->list[Mood]:
        sql = f"SELECT * FROM {self.db.moods_log_table_name};" if not columns else f"SELECT {columns} FROM {self.db.moods_log_table_name};"
        result = [Mood.from_record(record) for record in self.db.query(sql)]
        return result

    def last(self)->Mood|None:
        sql = f"SELECT {columns} FROM {self.db.moods_log_table_name} ORDER BY id DESC LIMIT 1;"
        result = self.db.query(sql)
        return Mood.from_record(result[0]) if len(result) else None

    def last_record(self, columns: str = '*')->tuple:
        sql = f"SELECT {columns} FROM {self.db.moods_log_table_name} ORDER BY id DESC LIMIT 1;"
        result = self.db.query(sql)
        return result[0] if len(result) else result
    
    def find_by_id(self, id: int|str)->Mood|None:
        sql = f"SELECT * FROM {self.db.moods_log_table_name} WHERE id = ?;"
        result = self.db.query(sql, (id,))
        return Mood.from_record(result[0])

    def search(self, criteria: dict)->list[Mood]|None: 
        conditions = []
        params = []
        sql = f"SELECT * FROM {self.db.moods_log_table_name}"
        for cli_column, value in criteria.items():
            db_column = self.map_cli_to_db(cli_column)
            if not db_column:
                return None
            
            column_type = self.db.get_db_column_type(self.db.moods_log_table_name, db_column)
            if not column_type:
                return None
            
            match str.lower(column_type):
                case 'text':
                    conditions.append(f"{db_column} LIKE ?")
                    params.append(f"%{value}%")
                case _:
                    conditions.append(f"{db_column} = ?")
                    params.append(value)
            
        query = f"{sql} {'WHERE ' if len(criteria.items()) else ''} {' AND '.join(conditions)}"
        return [Mood.from_record(record) for record in self.db.query(query, tuple(params))]

    def update(self, criteria: dict)->None:
        conditions = []
        params = []
        sql = f"UPDATE {self.db.moods_log_table_name} SET"
        
        for cli_column, value in criteria.items():
            db_column = self.map_cli_to_db(cli_column)
            if not db_column:
                return None
            
            if db_column == 'id':
                continue

            conditions.append(f"{db_column} = ?")
            params.append(value)

        params.append(criteria.get("id"))            
        query = f"{sql} {', '.join(conditions)} WHERE id = ?"
        self.db.query(query, tuple(params))
    
    def truncate(self, reset_sequence = True)->None:
        sql = f"DELETE FROM {self.db.moods_log_table_name};"
        self.db.query(sql)
        if reset_sequence:
            self.db.reset_schema(self.db.moods_log_table_name)

    def delete_last(self)->None:
        last_mood_id = self.last_record('id')
        self.db.query(f"DELETE FROM {self.db.moods_log_table_name} WHERE id IN (?)", last_mood_id)

    def delete_by_ids(self, ids: List[str|int])->None:
        self.db.query(f"DELETE FROM {self.db.moods_log_table_name} WHERE id IN ({'?,' * (len(ids) - 1)}?)", tuple(ids))

    def get_cli_columns(self)->List[str]:
        return self.cli_columns

    def map_cli_to_db(self, cli_column: str)->str|None:
        return self.cli_db_mapper[cli_column] if self.cli_db_mapper[cli_column] else None
