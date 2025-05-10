# MusiPy

A simple CLI Music / Moods Logger using Python

**Done as a fullfilment requirement for [MIT 6.100L: Introduction Into CS and Programming using Python](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/)**

- [Objectives](#objectives)
- [Extra Knowledge Gained](#extra-knowledge-gained)
- [Using Musipy](#using-musipy)

---

## Objectives

- Apply the OOP concepts and learn how to deal comfortably with custom data types (objects)
- Apply decomposition and abstraction in the code by creating modular, singly responsible functions

---

## Extra Knowledge Gained

- Learned a new python package (argparse, sqlite3)
- Learned how to make and deal with virtual environments to keep your code isolated
- Learned and applied more about repository design pattern
- Learned how to make a small CI/CD pipeline using Github Actions

---

## Using MusiPy

### Requirements

- Python 3.13

### Environment Setup

```bash
# 1. clone this repo
git clone https://github.com/abrahman-ra/musipy.git

# 2. go to the project directory
cd musipy/

# 3. create virtual environment
python3 -m venv venv

# 4. activate virtual environment
# LINUX & MACOS
source venv/bin/activate # if using fish as a shell, replace activate with activate.fish

# WINDOWS
.\venv\bin\activate.ps1
```

### Quick start

- **Note: Replace `python` command with `py` for windows**
- **Another Note: `$` indicates a command input, while `>>>` indicates command output**

```bash
$ python main.py

>>> Welcome to MusiPy! My first small step towards a big dream ❤️
>>> Let's start out journey 🎶😍
>>> 👤: Enter your name (Ctrl + C to exit): $ Abdurrahman
>>> Welcome Abdurrahman 🥰! We wish you a great experience using MusiPy ❤️
>>> Start with `python main.py mood -A "SONG NAME, CURRENT FEELING, OPTIONAL DETAILS"`
```

### Moods

- When dealing with moods, we use the `mood` subparser, feel free to dicover the command help

```bash
$ python main.py mood --help
```

#### Adding a new mood

```bash
$ python main.py mood -A "song = an example song, feeling = any feeling that I feel, notes = these are optional notes that you may or may not add"

>>> Yay 😍! You have added your very first mood with MusiPy 💖💖💖
>>> Mood Recorded ✅🎶
>>> 💕 [ID: 1] Feeling any feeling that i feel when listening to an example song, described as: "these are optional notes that you may or may not add" (at 2025-05-10 22:56:38)
```

#### Listing all moods

Use `-l` or `--list`

```bash
$ python main.py mood -l

>>> 🌌✨ [ID: 1] Feeling any feeling that i feel when listening to an example song, described as: "these are optional notes that you may or may not add" (at 2025-05-10 19:56:38)
```

#### Listing latest mood

Use `-L` or `--last`

```bash
$ python main.py mood --last

>>> 🌌✨ [ID: 1] Feeling any feeling that i feel when listening to an example song, described as: "these are optional notes that you may or may not add" (at 2025-05-10 19:56:38)
```

#### Searching for existing mood

- Use `-S` or `--search` when searchine for moods, at least one criteria must be required, either `id`, `mood`, `notes`, partial string search is supported

```bash
$ python main.py mood -S "song = example"

>>> 🌌✨ [ID: 1] Feeling any feeling that i feel when listening to an example song, described as: "these are optional notes that you may or may not add" (at 2025-05-10 19:56:38)
```

#### Updating an existing mood

- Use `-U` or `--update` followed by the id to be updated (required) and at least one column to be updated

```bash
$ python main.py mood -U "id = 1, song = updated song name"

>>> Mood with id 1 is updated successfully 🔃✅
>>> 🌌✨ [ID: 1] Feeling any feeling that i feel when listening to updated song name, described as: "these are optional notes that you may or may not add" (at 2025-05-10 19:56:38)
```

#### Delteing moods

Use `-D` or `--delete`, and you can either

- Delete all moods, by providing `*` or `all`
- Delete last mood, by providing `last`
- Delete some records, by providing a list of comma separated ids

```bash
$ python main.py mood -D last
>>> Last mood deleted successfully ⏮️

# or
$ python main.py mood -D all
>>> All moods deleted successfully 🗄️

# or
$ python main.py mood -D 1,2,3
>>> Moods with ids: [1, 2, 3] deleted successfully 🗑️
```

### User

#### Updating user data

Use `-U` with the new name

```bash
$ python main.py user -U newoo

>>> User Updated, New User Info 👇🏼: 
Authinticated user "newoo" with id = 1 (created at 2025-05-10 22:50:41)
```

#### Deleting user data (and with its moods)

- Use `-R` or `--reset`

```bash
$ python main.py -R

>>> Your user data and all the recorded moods will be lost
>>> Are you sure? y / N: 
$ y
>>> User and Moods deleted
>>> We are sad to see you go 😢💔
```