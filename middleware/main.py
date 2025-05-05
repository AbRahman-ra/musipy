from collections.abc import Callable
from start.main import user_repo

def auth_then(next: Callable[[any], any], *args)->any:
    if user_repo.auth:
        return parser.print_help()
    return next(*args)