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
        return f"User {'object' if not self.id else (f'record with id: {self.id}')} having name {self.name} (created at {self.created_at})"
