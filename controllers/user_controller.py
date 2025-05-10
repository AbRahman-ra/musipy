from start.main import user_repo, mood_repo
from models.user import User
from config.const import app_file_name

def welcome_user()->None:
    print("Welcome to MusiPy! My first small step towards a big dream ❤️")
    print("Let's start out journey 🎶😍")
    name = input("👤: Enter your name (Ctrl + C to exit): ")
    if not len(name):
        print("Oops! Name cannot be empty 😬")
        return
    add_new_user(name)

def reset_app()->None:
    print("Your user data and all the recorded moods will be lost")
    confirm = input("Are you sure? y / N: ")
    if confirm not in "Yy" or not len(confirm):
        print("Data not deleted!")
        return
    mood_repo.truncate()
    user_repo.delete(user_repo.info(), True)
    print("User and Moods deleted")
    print("We are sad to see you go 😢💔")

def all()->None:
    user = user_repo.info()
    print(f"current user 😇: {user}")

def add_new_user(name: str)->None:
    user = User(name)
    user_repo.add(user)
    show_post_signup_message(name)

def update_user(new_name: str)->None:
    user_repo.update(user_repo.info(), {
        "name": new_name
    })
    print(f"User Updated, New User Info 👇🏼: ")
    print(user_repo.info())

def show_post_signup_message(name: str):
    print(f"Welcome {name} 🥰! We wish you a great experience using MusiPy ❤️")
    print(f"Start with `python {app_file_name} mood -A \"SONG NAME, CURRENT FEELING, OPTIONAL DETAILS\"`")
