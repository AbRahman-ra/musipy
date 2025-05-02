from db.database import Database
from models.user import User
from models.mood import Mood
from repos.user_repo import UserRepository
from repos.mood_repo import MoodRepository

if __name__ == "__main__":
    # create database and run migrations if not exist
    db = Database()
    # print(db)

    # repo = MoodRepository(db)
    # mood = Mood("Sa3at", "emotional", "ILY Elissa")
    # repo.add(mood)
    # print(mood)
    # mood.add_mood(db)
    # print(repo.all())

    repo = UserRepository(db)
    user = User("Adult")
    repo.add(user)
    # repo.info()
    print(user)
    print(repo.info())
    print("#" * 10)
    repo.update(user, {
        "name": "Baby"
    })
    print(user)
    print(repo.info())
    print("#" * 10)
    # print()
    repo.delete(user, True)
    print("#" * 10)
    print(user)
    print(repo.info())

    # if no user, ask for data and store it
    # welcome user
