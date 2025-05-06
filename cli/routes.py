from cli.main import parser, args
from start.main import user_repo
from cli.helpers import handle_empty_command, handle_reset_command, handle_user_commands, handle_mood_commands


# determine if no input is given
non_empty_args = [val for val in vars(args).values() if val]
is_empty = len(non_empty_args) == 0

if is_empty:
    handle_empty_command()
elif args.entity == "user":
    handle_user_commands()
elif args.reset:
    handle_reset_command()
elif args.entity == "mood":
    handle_mood_commands()
else:
    pass