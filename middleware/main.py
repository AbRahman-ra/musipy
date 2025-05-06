from collections.abc import Callable
from start.main import user_repo
from config.const import app_file_name

def auth_then(next: Callable[[any], any], *args, fail: Callable[[any], any] = None, **fargs)->any:

    if not user_repo.auth:
        return fail(**fargs) if fail else None
    return next(*args)