from config.const import app_file_name
from cli.main import mood_parser
from start.main import user_repo, mood_repo
from typing import List

def invalid_cmd_no_auth()->None:
    print("Invalid Command ⚠️")
    print("You must add a user first!")
    print(f"Run `python {app_file_name} user -A YOUR_NAME`")

def invalid_mood_cmd()->None:
    print("Invalid Command, kindly attach it with one of the arguments!")
    mood_parser.print_help()

def invalid_cmd_user_exists()->None:
    print("Oops! Cannot add a new user 😬")
    print(f"user {user_repo.info().name} exists!")
    print(f"Run `python {app_file_name} user -U new_name` to update the name of current user, OR")
    print(f"Run `python {app_file_name} -R` to delete all the user's and moods' data")

def invalid_cmd_invalid_mood(record: dict)->None:
    print(f"The record {record} should have {mood_repo.num_required_fields} required fields, but {len(record)} was given")
    print("If you have spaces in your data, enclose everything in quotes")
    print(f"Example: `python {app_file_name} mood -A \"My Song, My Feeling, I have too much details to say\"`")

def invalid_cmd_incorrect_column()->None:
    print("Invalid Command!")
    print(f"Column must be in: {mood_repo.get_cli_columns()}")
    print("Note: mood/feeling are aliases, notes/details are aliases")
    print("Note: Partial search is supported")

def invalid_cmd_id_not_provided()->None:
    print("Invalid Command ❌, ID must be provided as a criteria")

def invalid_cmd_no_update_criteria_provided()->None:
    print("Invalid Command ❌, No update criteria provided")
