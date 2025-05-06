from start.main import user_repo, mood_repo
from cli.main import args
from models.user import User
from middleware.main import auth_then
import controllers.user_controller as uc
import controllers.mood_controller as mc

def handle_empty_command()->any:
    return auth_then(uc.welcome_user)

def handle_reset_command()->any:
    return auth_then(uc.reset_app)

def handle_user_commands()->any:
    if args.list:
        return auth_then(uc.all)
    elif args.add:
        return uc.add_new_user(args.add)
    elif args.update:
        return auth_then(uc.update_user, args.update)

def handle_mood_commands()->any:
    if args.list:
        return auth_then(mc.all)
    elif args.last:
        return auth_then(mc.last)
    elif args.search:
        pass
    elif args.add:
        pass
    elif args.update:
        pass
    elif args.delete:
        pass
    else:
        return auth_then(mc.invalid_cmd)


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
