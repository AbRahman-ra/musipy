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
    id: int = None

    @classmethod
    def from_record(cls, record: tuple)->"Mood":
        return cls(record[2], record[1], record[3], record[4], record[0])

    def __str__(self)->str:
        return f"{f'[ID: {self.id}]' if self.id else ''} Feeling {self.feeling} when listening to {self.song}, {f'described as: \"{self.description}\"' if len(self.description) else 'with no description'} (at {self.created_at})"
