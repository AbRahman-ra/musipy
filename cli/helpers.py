from cli.main import args, parser
from middleware.main import auth_then, no_auth_then, process_str_to_csv
import controllers.user_controller as uc
import controllers.mood_controller as mc

def handle_empty_command()->any:
    return auth_then(next=parser.print_help, fail=uc.welcome_user)

def handle_reset_command()->any:
    return auth_then(uc.reset_app)

def handle_user_commands()->any:
    if args.list:
        return auth_then(uc.all, fail=uc.invalid_cmd_no_auth)
    elif args.add:
        return no_auth_then(uc.add_new_user, args.add, fail=uc.invalid_cmd_user_exists)
    elif args.update:
        return auth_then(uc.update_user, args.update, fail=uc.invalid_cmd_no_auth)

def handle_mood_commands()->any:
    if args.list:
        return auth_then(mc.all, fail=uc.invalid_cmd_no_auth)
    elif args.last:
        return auth_then(mc.last, fail=uc.invalid_cmd_no_auth)
    elif args.search:
        pass
    elif args.add:
        return auth_then(process_str_to_csv, args.add, mc.add, fail=uc.invalid_cmd_no_auth)
    elif args.update:
        pass
    elif args.delete:
        pass
    else:
        return auth_then(mc.invalid_cmd)
