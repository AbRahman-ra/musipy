from cli.main import args, parser
from middleware.main import auth_then, no_auth_then, validate_new_mood, process_data_to_dict, handle_deletion_criteria, check_mood_id_exists
from middleware.fail import invalid_mood_cmd
import controllers.user_controller as uc
import controllers.mood_controller as mc

def handle_empty_command()->any:
    return auth_then(next=parser.print_help, fail=uc.welcome_user)

def handle_reset_command()->any:
    return auth_then(uc.reset_app)

def handle_user_commands()->any:
    if args.list:
        return auth_then(uc.all)
    elif args.add:
        return no_auth_then(uc.add_new_user, args.add)
    elif args.update:
        return auth_then(uc.update_user, args.update)

def handle_mood_commands()->any:
    if args.list:
        return auth_then(mc.all)
    elif args.last:
        return auth_then(mc.last)
    elif args.search:
        return auth_then(process_data_to_dict, args.search, mc.search)
    elif args.add:
        return auth_then(process_data_to_dict, args.add, validate_new_mood, mc.add)
    elif args.update:
        return auth_then(process_data_to_dict, args.update, check_mood_id_exists, mc.update)
    elif args.delete:
        return auth_then(handle_deletion_criteria, args.delete, mc.delete)
    else:
        return auth_then(invalid_mood_cmd)
