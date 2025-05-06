from collections.abc import Callable
from start.main import user_repo
from config.const import app_file_name

def auth_then(next: Callable[[any], any], *args, fail: Callable[[any], any] = None, **fargs)->any:
    if not user_repo.auth:
        return fail(**fargs) if fail else None
    return next(*args)

def no_auth_then(next: Callable[[any], any], *args, fail: Callable[[any], any] = None, **fargs)->any:
    if not user_repo.auth:
        return next(*args)
    return fail(**fargs) if fail else None

def process_str_to_csv(command: str, next: Callable[[any, any], any], *args, fail: Callable[[any], any] = None, **fargs):
    new_command = [field.strip() for field in command.split(",") if len(field.strip())]
    return next(new_command, *args)
