from django.contrib.auth.models import User
from .models import Note, Category

# User
def get_user_by_username(username):
    return User.objects.filter(username=username).first()

def create_user(username, email, password):
    return User.objects.create_user(username=username, email=email, password=password)

# Get all notes and one note
def all_notes(user):
    return Note.objects.filter(user = user)

def note_by_id(note_id, user):
    return Note.objects.filter(id=note_id, user=user).first()

# Create / edit / delete notes
def create_note(title,content,categories,user):
    note = Note.objects.create(title=title,content=content,user=user)
    note.categories.set(categories)
    return note

def edit_note(note,title,content):
    note.title = title
    note.content = content
    note.save()
    return note

def delete_note(note):
    return note.delete()

# Archive / unarchive notes
def archive_or_unarchive_note(note,is_archived):
    note.is_archived = is_archived
    note.save()
    return note

# List active notes
def active_notes(user):
    return Note.objects.filter(user=user, is_archived=False)

# List archived notes
def archived_notes(user):
    return Note.objects.filter(user=user, is_archived=True)

def create_category(category_name):
    category = Category.objects.get_or_create(name=category_name)
    return category

#Search category
def search_category(id):
    return Category.objects.get(id=id)

# Add / Remove category
def add_category(note,categories):
    for category_name in categories:
        category, _ = create_category(category_name)
        note.categories.add(category)
    note.save()
    return note

def remove_category(note,categories):
    for category_id in categories:
        category = search_category(category_id)
        note.categories.remove(category)
    note.save()
    return note

# Filter category by user
def filter_categories_by_user(user):
    return Category.objects.filter(note__user=user).distinct()

# Filter notes by category
def filter_notes_by_category(user, category_id):
    return Note.objects.filter(user=user, categories__id=category_id)