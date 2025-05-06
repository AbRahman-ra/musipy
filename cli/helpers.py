from cli.main import args, parser
from middleware.main import auth_then
import controllers.user_controller as uc
import controllers.mood_controller as mc

def handle_empty_command()->any:
    return auth_then(next=parser.print_help, fail=uc.welcome_user)

def handle_reset_command()->any:
    return auth_then(uc.reset_app)

def handle_user_commands()->any:
    if args.list:
        return auth_then(next=uc.all)
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
