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

def add(record: dict)->None:
    mood = mood_repo.create_mood_from_cli(record)
    mood_repo.add(mood)
    if mood.id == 1:
        show_1st_mood_motivational_message()
    show_mood_added_success_message(mood)

def show_mood(mood: Mood)->None:
    print(f"🌌✨ {mood}")

def search(data: dict)->None:
    result = mood_repo.search(data)
    for mood in result:
        show_mood(mood)

def delete(criteria: str|List[str]):
    if type(criteria) == str:
        if criteria in ['all', '*']:
            print("Note: The default behavior is to reset sequence IDs (i.e start counting ids from 1 after deletion)")
            confirm = input("Write [N] if you want to prevent resetting the ids, click any button to force the system defaults")
            reset = confitm == 'N'
            mood_repo.truncate(reset)
            print("All moods deleted successfully 🗄️")
        elif criteria == 'last':
            mood_repo.delete_last()
            print(f"Last mood deleted successfully ⏮️")
        return
    mood_repo.delete_by_ids(criteria)
    print(f"Moods with ids: {criteria} deleted successfully 🗑️")

def update(data: dict)->None:
    mood_repo.update(data)
    mood_id = data.get("id")
    new_mood = mood_repo.find_by_id(mood_id)
    print(f"Mood with id {mood_id} is updated successfully 🔃✅" if new_mood else f"No mood associated with the id {mood_id}, so no moods updated 🪹")
    if new_mood:
        show_mood(new_mood)

def show_no_moods_message()->None:
    print("No moods yet, start adding your first mood now 😍")
    print(f"Example: `python {app_file_name} mood -A \"My Song, My Feeling, I have too much details to say\"`")

def show_1st_mood_motivational_message()->None:
    print(f"Yay 😍! You have added your very first mood with MusiPy 💖💖💖")

def show_mood_added_success_message(mood: Mood):
    print(f"Mood Recorded ✅🎶")
    print(f"💕 {mood}")