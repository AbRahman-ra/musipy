import argparse

parser = argparse.ArgumentParser(
    prog="Musipy",
    description="A simple CLI logging application to track your mood and songs"
)

# entities
entities_group = parser.add_mutually_exclusive_group()
entities_group.add_argument("-m", "--mood", action="store_true")
entities_group.add_argument("-U", "--user", action="store_true")
entities_group.add_argument("-R", "--reset", action="store_true", help="Delete all the data (moods and user)")

general_group = parser.add_mutually_exclusive_group()
general_group.add_argument("-l", "--list", action='store_true', help="List all moods")
general_group.add_argument("-S", "--search", help="search moods")

entities_multi_input_group = parser.add_argument_group()
entities_multi_input_group.add_argument("-A", "--add", help="Add New [mood / user]")
entities_multi_input_group.add_argument("-u", "--update", help="Update [mood / user]")
entities_multi_input_group.add_argument("-K", "--key", help="Column identification (in add/search/update function [comma separated])")
entities_multi_input_group.add_argument("-V", "--value", help="Column value (in add/search/update function [comma separated])")
entities_multi_input_group.add_argument("-D", "--delete", action="store_true", help="Delete all moods")
entities_multi_input_group.add_argument("-O", "--only", help="List specific columns [comma separated]")

args = parser.parse_args()