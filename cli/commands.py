from cli.helpers import welcome_user, show_moods, show_user_info, delete_everything
from cli.main import parser, args
from start.main import user_repo
from repos.mood_repo import MoodRepository

is_empty = True

for value in vars(args).values():
    if value:
        is_empty = False
        break

if is_empty:
    parser.print_help()

if not user_repo.info():
    welcome_user()

elif args.mood:
    if args.list:
        show_moods(args.only) if args.only else show_moods()
    elif args.search:
        handle_search_moods(args.key, args.value)
    elif args.delete:
        delete_all_moods()

elif args.user:
    if args.list:
        show_user_info()

elif args.reset:
    delete_everything()
