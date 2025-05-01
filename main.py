from db.database import Database
from models.mood import Mood, MoodRepository
from models.user import User, UserRepository

if __name__ == "__main__":
    # create database and run migrations if not exist
    db = Database()
    # print(db)

    # repo = MoodsRepository(db)
    # mood = Mood("Sa3at", "emotional", "ILY Elissa")
    # repo.add(mood)
    # print(mood)
    # mood.add_mood(db)
    # print(repo.all())

    repo = UsersRepository(db)
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
    repo.delete(user)
    print("#" * 10)
    print(user)
    print(repo.info())

    # if no user, ask for data and store it
    # welcome user
