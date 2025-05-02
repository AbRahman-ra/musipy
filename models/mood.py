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
