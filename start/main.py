from db.database import Database
from repos.user_repo import UserRepository
from repos.mood_repo import MoodRepository

db = Database()
user_repo = UserRepository(db)
mood_repo = MoodRepository(db)
