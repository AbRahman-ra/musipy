from db.database import Database
from models.user import User

class UserRepository:
    db = None
    
    def __init__(self, db: Database):
        self.db = db

    def add(self, user: User)->None:
        sql = f"INSERT INTO {self.db.user_table_name} (name, created_at, updated_at) VALUES (?, ?, ?)"
        params = (user.name, user.created_at, user.created_at)
        self.db.query(sql,params)
        user.id = self.db.query("SELECT last_insert_rowid()")[0][0]

    def info(self)->User|None:
        result = self.db.query(f"SELECT * FROM {self.db.user_table_name};")
        if len(result):
            return User.from_row(result[0])
        return None

    def update(self, user: User, data: dict)->None: 
        set_clauses = []
        params = []

        for key, val in data.items():
            set_clauses.append(f"{key} = ?")
            params.append(val)
            setattr(user, key, val)

        # Always update updated_at
        set_clauses.append("updated_at = CURRENT_TIMESTAMP")

        sql = f"UPDATE {self.db.user_table_name} SET {', '.join(set_clauses)} WHERE id = ?"
        params.append(user.id)

        self.db.query(sql, tuple(params))

    def delete(self, user: User, reset_sequence: bool = False)->None:
        sql = f"DELETE FROM {self.db.user_table_name} WHERE id = ?"
        params = (user.id,)
        self.db.query(sql, params)
        user.id = None
        if reset_sequence:
            self.reset_schema()
    
    def reset_schema()->None:
        sql = f"DELETE FROM sqlite_sequence WHERE name = ?;"
        params = (self.db.user_table_name,)
        self.db.query(sql, params)
