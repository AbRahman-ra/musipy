from db.database import Database
from models.user import User
from models.mood import Mood
from repos.user_repo import UserRepository
from repos.mood_repo import MoodRepository
import cli.commands

if __name__ == "__main__":

    pass
    # flow
    # 1. Welcome the user if not exists (add auth layer before all routes)
    # 2. If user exists and no args, show help menu
    # 3. Commands
    #    # 1. --list
    #    # 2. --add
    #    # 3. --search
    #    # 4. --reset-moods
    #    # 5. --add-user
    #    # 6. --update-user
    #    # 7. --delete-everything
    # create database and run migrations if not exist
    # db = Database()
    # print(db)

    # repo = MoodRepository(db)
    # mood = Mood("Sa3at", "emotional", "ILY Elissa")
    # repo.add(mood)
    # print(mood)
    # mood.add_mood(db)
    # print(repo.all())

    # repo = UserRepository(db)
    # user = User("Adult")
    # repo.add(user)
    # # repo.info()
    # print(user)
    # print(repo.info())
    # print("#" * 10)
    # repo.update(user, {
    #     "name": "Baby"
    # })
    # print(user)
    # print(repo.info())
    # print("#" * 10)
    # # print()
    # repo.delete(user, True)
    # print("#" * 10)
    # print(user)
    # print(repo.info())

    # if no user, ask for data and store it
    # welcome user
