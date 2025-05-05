from start.main import mood_repo
from typing import List
from models.mood import Mood

def all()->None:
    moods = mood_repo.info()
    if not len(moods):
        print("No moods yet, start adding your first mood now 😍")
    else:
        for m in moods:
            print(f"🌌✨ {mood}")