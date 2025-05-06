from collections.abc import Callable
from start.main import user_repo
from config.const import app_file_name

def auth_then(next: Callable[[any], any], *args)->any:
    if not user_repo.auth:
        print("You have to add a user first")
        print(f"Run `python {app_file_name} user -A <YOUR_NAME>`")
        return
    return next(*args)