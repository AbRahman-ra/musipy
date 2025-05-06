from dataclasses import dataclass
from datetime import datetime
from typing import Optional

# user object
@dataclass
class User:
    name: str
    created_at: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    id: Optional[int] = None

    @classmethod
    def from_row(cls, row: tuple)->"User":
        return cls(id=row[0], name=row[1], created_at=row[2])

    def __str__(self)->str:
        return f"{'Authinticated user' if self.id else 'Non-authinticated user'} \"{self.name}\" {f'with id = {self.id} ' if self.id else ''}(created at {self.created_at})"
