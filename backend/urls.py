from django.urls import path
# Authentication views
from .views import LoginView, RegisterView, LogoutView
# Note management views: display, create, edit, delete
from .views import HomeView, SeeNoteView, CreateNoteView, EditNoteView, DeleteNoteView
# Note archive management views
from .views import ArchiveView, UnarchiveView, ListActiveView, ListArchiveView
# Category management views: list, add, remove, filter
from .views import ListCategoriesView, AddCategoriesView, RemoveCategoriesView, FilterCategoriesView

urlpatterns = [
    # Login / Register / Logout
    path('', LoginView.as_view(), name='login'),  # Login page
    path('register/', RegisterView.as_view(), name='register'),  # User registration
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout user

    # Get all or one note. Create / edit / delete notes 
    path('home/', HomeView.as_view(), name='home'),  # User's home with all notes
    path('note/<int:id>/', SeeNoteView.as_view(), name='note'),  # View a specific note by ID
    path('create_note/', CreateNoteView.as_view(), name='create_note'),  # Create a new note
    path('edit_note/<int:id>/', EditNoteView.as_view(), name='edit_note'),  # Edit an existing note
    path('delete_note/<int:id>/', DeleteNoteView.as_view(), name='delete_note'),  # Delete a note

    # Archive / Unarchive notes. List active / archived notes
    path('archive_note/<int:id>/', ArchiveView.as_view(), name='archive_note'),  # Archive a note
    path('unarchive_note/<int:id>/', UnarchiveView.as_view(), name='unarchive_note'),  # Unarchive a note
    path('list_active_view', ListActiveView.as_view(), name='list_active_view'),  # List active (non-archived) notes
    path('list_archived_view', ListArchiveView.as_view(), name='list_archived_view'),  # List archived notes

    # List / Add / remove categories. Filter categories by user . Filter notes by catergory.
    path('list_categories/<int:id>/', ListCategoriesView.as_view(), name='list_categories'),  # List categories of a note
    path('add_categories/<int:id>/', AddCategoriesView.as_view(), name='add_categories'),  # Add categories to a note
    path('remove_categories/<int:id>/', RemoveCategoriesView.as_view(), name='remove_categories'),  # Remove categories from a note
    path('filter_categories/', FilterCategoriesView.as_view(), name='filter_categories'),  # Filter notes by category
]