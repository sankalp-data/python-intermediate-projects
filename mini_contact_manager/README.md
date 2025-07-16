A simple and functional Contact Book application written in Python.
It uses a JSON file as a persistent database to perform basic contact management operations like:

 - Adding contacts

 - Viewing all contacts

 - Searching contacts

 - Deleting contacts

 - Updating existing contacts


# **Features**

 - Add multiple contacts at once

 - Search contacts by name (case-insensitive)

 - Display all contacts in a formatted view

 - Delete contacts by name

 - Update existing contact details

 - Stores contacts in contacts.json (in the same directory)

# How to Run

1. Make sure you have Python 3.x installed.

2. Place the script in a folder.

3. Open terminal and run:

 - python mini_contact_manager.py


# **Concepts Used**

 - JSON file read/write (json module)

 - List and dictionary operations

 - String manipulation and formatting

 - File handling with exception safety

 - Modular and readable function-based structure

 - Input validation (try/except)

# **Error Handling**

 - Prevents app crash on:

 - File not found (FileNotFoundError)

 - Empty or corrupted JSON (JSONDecodeError)

 - Invalid numeric inputs (ValueError)

 - Gracefully handles invalid menu choices