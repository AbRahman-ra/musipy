from collections.abc import Callable
from start.main import user_repo, mood_repo
from config.const import app_file_name
from middleware.fail import *
from typing import List

# user middleware
def auth_then(next: Callable[[any], any], *args, fail: Callable[[any], any] = None, **fargs)->any:
    if not user_repo.auth:
        return invalid_cmd_no_auth() if not fail else fail(**fargs)
    return next(*args)

def no_auth_then(next: Callable[[any], any], *args)->any:
    if not user_repo.auth:
        return next(*args)
    return invalid_cmd_user_exists()


# moods middleware
def process_str_to_csv(command: str, next: Callable[[any, any], any], *args):
    new_command = [field.strip() for field in command.split(",") if len(field.strip())]
    return next(new_command, *args)

def process_data_to_dict(command: str, next: Callable[[any, any], any], *args)->any:
    criteria = [field.strip() for field in command.split(",") if len(field.strip())]
    data = {}
    for search in criteria:
        data_list = [str.lower(field.strip()) for field in search.split("=") if len(field.strip())]
        if len(data_list) < 2 or data_list[0] not in mood_repo.get_cli_columns():
            return invalid_cmd_incorrect_column()
        data[data_list[0]] = data_list[1]
    return next(data, *args)

def handle_deletion_criteria(command: str, next: Callable[[any], any], *args)->any:
    command = str.lower(command)
    return (
        next(command) if command in ['all', '*', 'last'] else process_str_to_csv(command, next, *args)
    )

def validate_new_mood(record: dict, next: Callable[[any], any], *args)->any:
    return next(record, *args) if len(record.keys()) >= mood_repo.num_required_fields else invalid_cmd_invalid_mood(record)

def check_mood_id_exists(record: dict, next: Callable[[any], any], *args)->any:
    if not record.get("id"):
        return invalid_cmd_id_not_provided()
    if len(record.items() < 2):
        return invalid_cmd_no_update_criteria_provided()
    return next(record, *args)
