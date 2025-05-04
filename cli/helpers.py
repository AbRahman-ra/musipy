from start.main import user_repo
from start.main import mood_repo
from models.user import User

def welcome_user()->None:
    print("Welcome to MusiPy! My first small step towards a big dream ❤️")
    print("Let's start out journey 🎶😍")
    name = input("👤: Enter your name (Ctrl + C to exit): ")
    if not len(name):
        print("Oops! Name cannot be empty 😬")
        return
    user = User(name)
    user_repo.add(user)
    print(f"Welcome {name} 🥰! We wish you a great experience using MusiPy ❤️")
    print("Start with `python --mood --add --key=song,feeling --value='Ya Layali','sensual'`")

def show_moods(columns: str = None)->None:
    moods = mood_repo.all(columns)
    if not len(moods):
        print("No moods yet, start adding your first mood now 😍")
    else:
        for mood in moods:
            print(f"* {mood}")

def show_user_info()->None:
    user = user_repo.info()
    print(user)

def delete_everything()->None:
    confirm = input("Are you sure? y / N")
    if confirm == "y":
        mood_repo.truncate()
        user_repo.delete(user_repo.info(), True)
        print("User and Moods deleted successfully")
    else:
        print("Data not deleted!")

def handle_search_moods(key: str|None, value: str|None)->None:
    if (not key and not value) or (not len(key) and not len(value)):
        return show_moods()
    
    key_list = key.split(",")
    value_list = value.split(",")

    if len(key_list) != len(value_list):
        print("Number of parameters to search in key and value is not equivalent")
        return
    
    moods = mood_repo.multi_search(key_list, value_list)
    for mood in moods:
        print(f"* {mood}")
