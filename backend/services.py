from django.contrib.auth import authenticate, login, logout

# Import functions for data manipulation by users
from .repositories import create_user, get_user_by_username
# Import functions for data manipulation by notes 
from .repositories import all_notes, create_note, note_by_id, edit_note, delete_note
# Import functions for data manipulation by active / archived notes 
from .repositories import  archive_or_unarchive_note, active_notes, archived_notes
# Import functions for data manipulation by category 
from .repositories import add_category, remove_category, filter_categories_by_user ,filter_notes_by_category

#
## Login / Register
#

# Attempts to authenticate and log in a user. Returns True if successful, otherwise False.
def try_login(request, username, password):
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return True
    return False

# Registers a new user if the username is not already taken. Returns the created user or None if the username already exists.
def register_user(username, email, password):
    if get_user_by_username(username):
        return None
    return create_user(username, email, password)

#Log out
def perform_logout(request):
    logout(request)

#
## Get all or one note. Create / edit / delete notes 
#

# Retrieves all notes associated with the given user.
def get_all_notes(user):
    return all_notes(user)

# Retrieves a specific note by ID, only if it belongs to the user.
def get_note(note_id, user):
    note = note_by_id(note_id, user)
    if note:
        return note
    return None

# Creates a new note with the given title, content, categories, and username.
def post_add_note(username, title, content, categories=None):
    if categories is None:
        categories = []
    return create_note(title,content,categories,username)

# Updates an existing note if it belongs to the user. Returns the updated note or None if not found.
def post_update_note(note_id, user, title, content):
    note = note_by_id(note_id, user)
    if note:
        return edit_note(note,title,content)
    return None

# Deletes a note if it belongs to the user. Returns the result of the deletion or None if not found.
def post_remove_note(note_id, user):
    note = note_by_id(note_id, user)
    if note:
        return delete_note(note)
    return None

#
## Archive / Unarchive notes. List active / archived notes
#

# Archives a note if it belongs to the user.
def post_archive_note(note_id, user):
    note = note_by_id(note_id, user)
    if note:
        return archive_or_unarchive_note(note,True)
    return None

# Unarchives a note if it belongs to the user.
def post_unarchive_note(note_id, user):
    note = note_by_id(note_id, user)
    if note:
        return archive_or_unarchive_note(note,False)
    return None

# Retrieves all active (non-archived) notes for the user.
def get_active_notes(user):
    return active_notes(user)

# Retrieves all archived notes for the user.
def get_archived_notes(user):
    return archived_notes(user)

#
## Add / remove categories. Filter categories by user . Filter notes by catergory.
#

# Adds new categories to a note if it belongs to the user.
def post_add_categories(note_id, user, categories_name):
    note = note_by_id(note_id, user)
    if note:
        return add_category(note, categories_name)
    return None

# Removes categories from a note if it belongs to the user.
def post_remove_categories(note_id, user, categories_ids):
    note = note_by_id(note_id, user)
    if note:
        return remove_category(note, categories_ids)
    return None

# Retrieves all categories associated with the user.
def get_user_categories(user):
    return filter_categories_by_user(user)

# Filters the user's notes by a specific category.
def get_filter_categories(user,category_id):
    return filter_notes_by_category(user,category_id)