from start.main import user_repo, mood_repo
from models.user import User

def welcome_user()->None:
    print("Welcome to MusiPy! My first small step towards a big dream ❤️")
    print("Let's start out journey 🎶😍")
    name = input("👤: Enter your name (Ctrl + C to exit): ")
    if not len(name):
        print("Oops! Name cannot be empty 😬")
        return
    add_new_user(name)
    show_post_signup_message(name)

def reset_app()->None:
    confirm = input("Are you sure? y / N: ")
    if confirm not in "Yy" or not len(confirm):
        print("Data not deleted!")
        return
    mood_repo.truncate()
    user_repo.delete(user_repo.info(), True)
    print("User and Moods deleted successfully")

def all()->None:
    user = user_repo.info()
    print(f"current user 😇: {user}")

def add_new_user(name: str)->None:
    user = User(name)
    user_repo.add(user)
    show_post_signup_message(name)

def update_user(new_name: str)->None:
    user_repo.update(user_repo.info(), {
        name: new_name
    })

def show_post_signup_message(name: str):
    print(f"Welcome {name} 🥰! We wish you a great experience using MusiPy ❤️")
    print("Start with `python --mood --add --key=song,feeling --value='Ya Layali','sensual'`")
