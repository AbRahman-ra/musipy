from start.main import mood_repo
from typing import List
from models.mood import Mood
from cli.main import mood_parser
from typing import List
from config.const import app_file_name

def all()->None:
    moods = mood_repo.all()
    if not len(moods):
        show_no_moods_message()
        return
    for m in moods:
        show_mood(m)

def last()->None:
    last_mood = mood_repo.last()
    show_mood(last_mood) if last_mood else show_no_moods_message()

def add(record: List[str])->None:
    is_valid = validate_new_mood(record)
    if not is_valid:
        return show_invalid_mood_msg(record)
    mood = Mood(record[0], record[1], record[2] if len(record) > 2 else "")
    mood_repo.add(mood)
    if mood.id == 1:
        show_1st_mood_motivational_message()
    show_mood_added_success_message(mood)

def show_mood(mood: Mood)->None:
    print(f"🌌✨ {mood}")

def invalid_cmd()->None:
    print("Invalid Command, kindly attach it with one of the arguments!")
    mood_parser.print_help()

def show_no_moods_message()->None:
    print("No moods yet, start adding your first mood now 😍")
    print(f"Example: `python {app_file_name} mood -A \"My Song, My Feeling, I have too much details to say\"`")

def validate_new_mood(record: List[str])->bool:
    return len(record) >= mood_repo.num_required_fields

def show_invalid_mood_msg(record: List[str])->None:
    print(f"The record {record} should have {mood_repo.num_required_fields} required fields, but {len(record)} was given")
    print("If you have spaces in your data, enclose everything in quotes")
    print(f"Example: `python {app_file_name} mood -A \"My Song, My Feeling, I have too much details to say\"`")

def show_1st_mood_motivational_message()->None:
    print(f"Yay 😍! You have added your very first mood with MusiPy 💖💖💖")

def show_mood_added_success_message(mood: Mood):
    print(f"Mood Recorded ✅🎶")
    print(f"💕 {mood}")