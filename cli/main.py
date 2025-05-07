import argparse
from config.const import app_name

parser = argparse.ArgumentParser(
    prog="musipy.py",
    description="A simple CLI logging application to track your mood and songs",
    epilog="run `python musipy user --help` or `python musipy mood --help` to show help menus for both user and mood"
)

entities_subparser = parser.add_subparsers(dest="entity")

# users rules
user_parser = entities_subparser.add_parser("user")
user_group = user_parser.add_mutually_exclusive_group()
user_group.add_argument("-l", "--list", "-I", "--info", action="store_true", help="Get the user information (if user exists!)")
user_group.add_argument("-A", "--add", metavar="<NAME>", help="Add a new user (if it doesn't exist)")
user_group.add_argument("-U", "--update", metavar="<NEW_NAME>", help="Set a new name for the user (if user exists!)")
# reset doesn't require "user" arg
parser.add_argument("-R", "--reset", action="store_true", help="Delete Everything (user and recorded moods)")

###

# moods rules
mood_parser = entities_subparser.add_parser("mood")
mood_group = mood_parser.add_mutually_exclusive_group()
mood_group.add_argument("-A", "--add", metavar="\"song = <SONG NAME>, feeling (alias: mood) = <FEELING>, details (alias: notes) = <DETAILS [OPTIONAL]>\"", help="Add a new mood")
mood_group.add_argument("-l", "--list", action="store_true", help="Display all moods")
mood_group.add_argument("-L", "--last", action="store_true", help="Display last inserted mood")
mood_group.add_argument("-S", "--search", metavar="\"id = <ID>, song = <SONG>, feeling (alias: mood) = <FEELING>, details (alias: notes) = <DETAILS>\"", help="at least 1 field must be provided, partial string search supported")
mood_group.add_argument("-U", "--update", metavar="\"id = <ID>, song = <NEW_SONG>, feeling (alias: mood) = <NEW_FEELING>, details (alias: notes) = <NEW_DETAILS>\"", help="if ID doesn't exist, no updates will happen, ID and at least one field are required")
mood_group.add_argument("-D", "--delete", metavar="<ID1>,<ID2>,<ID3>,... | last | all (alias: *)", help="if ID doesn't exist, no deletion will happen, if 'all' or 'last' keyword is provided, all/last moods will be deleted accordingly")


args = parser.parse_args()
