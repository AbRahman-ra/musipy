from db.database import Database
from models.user import User

class UserRepository:
    db = None
    auth = False
    
    def __init__(self, db: Database):
        self.db = db
        self.auth = bool(self.info())

    def add(self, user: User)->None:
        sql = f"INSERT INTO {self.db.user_table_name} (name, created_at, updated_at) VALUES (?, ?, ?)"
        params = (user.name, user.created_at, user.created_at)
        self.db.query(sql,params)
        user.id = self.db.query("SELECT last_insert_rowid()")[0][0]
        self.auth = True

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

    def delete(self, user: User, reset_sequence: bool = True)->None:
        sql = f"DELETE FROM {self.db.user_table_name} WHERE id = ?"
        params = (user.id,)
        self.db.query(sql, params)
        user.id = None
        self.auth = False
        if reset_sequence:
            self.db.reset_schema(self.db.user_table_name)

    def __str__(self):
        return f"User Repo for {'auth' if self.auth else 'no_auth'} user having {'no ' if not self.db else ''}db connection"
