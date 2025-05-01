from db.database import Database
from models.mood import Mood

if __name__ == "__main__":
    # create database and run migrations if not exist
    db = Database()
    print(db)
    mood = Mood("Zippy", "sad", "kossommak")
    # mood.add_mood(db)
    # print(mood)
    # mood.add_mood(db)
    # print(mood.list_moods(db))
    print(mood.search_moods(db, 'mood', 'h'))

    # if no user, ask for data and store it
    # welcome user
