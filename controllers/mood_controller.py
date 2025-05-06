from start.main import mood_repo
from typing import List
from models.mood import Mood
from cli.main import mood_parser

def all()->None:
    moods = mood_repo.info()
    if not len(moods):
        show_no_moods_message()
        return
    for m in moods:
        show_mood(m)

def last()->None:
    last_mood = mood_repo.last()
    show_mood(last_mood) if last_mood else show_no_moods_message() 

def show_mood(mood: Mood)->None:
    print(f"🌌✨ {mood}")

def invalid_cmd()->None:
    print("Invalid Command, kindly attach it with one of the arguments!")
    mood_parser.print_help()

def show_no_moods_message()->None:
    print("No moods yet, start adding your first mood now 😍")
