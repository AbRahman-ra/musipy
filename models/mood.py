from db.database import Database
from dataclasses import dataclass
from datetime import datetime

# mood object
@dataclass
class Mood:
    song: str
    feeling: str
    description: str = ""
    created_at: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self)->str:
        return f"Feeling {self.feeling} when listening to {self.song}, {('described as: ' + self.description) if len(self.description) else 'with no description'} at {self.created_at}"
