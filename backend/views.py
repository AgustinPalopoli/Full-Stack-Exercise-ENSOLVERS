from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm, NoteForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Messages
from django.contrib import messages

# Auth-related service functions
from .services import try_login, register_user, perform_logout
# Note CRUD operations
from .services import get_all_notes, get_note, post_add_note, post_update_note, post_remove_note
# Note archive management
from .services import post_archive_note, post_unarchive_note, get_active_notes, get_archived_notes
# Category management for notes
from .services import post_add_categories, post_remove_categories, filter_categories_by_user, filter_notes_by_category

#
## Login / Register
#

# Handles user login.
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        return render(request, 'backend/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            success = try_login(request, **form.cleaned_data)
            if success:
                return redirect('home')
            else:
                messages.error(request, "Incorrect username or password")
        return render(request, 'backend/login.html', {'form': form})

# Handles user registration.
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'backend/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = register_user(**form.cleaned_data)
            if user:
                return redirect('login')
            else:
                messages.error(request, "User alredy exists")
        return render(request, 'backend/register.html', {'form': form})

#Handles logout
class LogoutView(View):
    def get(self, request):
        perform_logout(request)
        return redirect('login')

#
## Get all or one note. Create / edit / delete notes 
#

# Shows all notes for the logged-in user.
@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request):
        notes = get_all_notes(user = request.user)
        user_categories = filter_categories_by_user(request.user)
        return render(request, 'backend/home.html', {'notes': notes,'categories':user_categories})

# Displays a single note by ID.
@method_decorator(login_required, name='dispatch')
class SeeNoteView(View):
    def get(self, request, id):
        note = get_note(note_id = id,user = request.user)
        if note:
            return render(request, 'backend/note.html', {'note': note})
        else:
            messages.error(request, "Error not existing note")
            return redirect('home')

# Handles note creation.
@method_decorator(login_required, name='dispatch')
class CreateNoteView(View):
    def get(self, request):
        form = NoteForm()
        return render(request, 'backend/create_note.html', {'form': form})
    
    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            note = post_add_note(request.user,**form.cleaned_data)
        return redirect('note', id=note.id)

# Handles note editing.
@method_decorator(login_required, name='dispatch')
class EditNoteView(View):
    def get(self, request, id):
        obj = get_note(id,request.user)
        if obj:
            form = NoteForm(instance=obj)
            return render(request, 'backend/edit_note.html', {'form': form})
        else:
            messages.error(request, "Error not existing note")
            return redirect('home')
        
    
    def post(self, request, id):
        form = NoteForm(request.POST)
        if form.is_valid():
            note = post_update_note(id, request.user,**form.cleaned_data)
            if note:
                return redirect('note', id=note.id)
            else:
                messages.error(request, "Error not existing note")
                return redirect('home')
            
        

# Handles note deletion.
@method_decorator(login_required, name='dispatch')
class DeleteNoteView(View):
    def post(self, request, id):
        note = post_remove_note(id,request.user)
        if not note:
            messages.error(request, "Error not existing note")
        return redirect('home')
        

#
## Archive / Unarchive notes. List active / archived notes
# 

# Archives a note.
@method_decorator(login_required, name='dispatch')
class ArchiveView(View):
    def post(self, request, id):
        note = post_archive_note(id,request.user)
        if not note:
            messages.error(request, "Error not existing note")
        return redirect('home')

# Unarchives a note.
@method_decorator(login_required, name='dispatch')
class UnarchiveView(View):
    def post(self, request, id):
        note = post_unarchive_note(id,request.user)
        if not note:
            messages.error(request, "Error not existing note")
        return redirect('home')

# Lists all active (non-archived) notes.
@method_decorator(login_required, name='dispatch')
class ListActiveView(View):
    def get(self, request):
        notes = get_active_notes(request.user)
        return render(request, 'backend/list_notes.html', {'notes': notes,'type': "Active"})

# Lists all archived notes.
@method_decorator(login_required, name='dispatch')
class ListArchiveView(View):
    def get(self, request):
        notes = get_archived_notes(request.user)
        return render(request, 'backend/list_notes.html', {'notes': notes,'type': "Archived"})
    
#
## List / Add / remove categories. Filter categories by user . Filter notes by catergory.
#

# Lists all categories for the user's note.
@method_decorator(login_required, name='dispatch')
class ListCategoriesView(View):
    def get(self, request, id):
        note = get_note(id,request.user)
        return render(request, 'backend/list_categories.html', {'note':note,'categories': note.categories})

# Adds categories to a note.  
@method_decorator(login_required, name='dispatch')
class AddCategoriesView(View):
    def post(self, request, id):
        note = get_note(id,request.user)
        new_categories = request.POST.getlist('add_categories')
        note = post_add_categories(id,request.user, new_categories)
        if note:
            return redirect('list_categories', id=note.id)
        else:
            messages.error(request, "Error not existing note")
            return redirect('home')

# Removes categories from a note.
@method_decorator(login_required, name='dispatch')
class RemoveCategoriesView(View):
    def post(self, request, id):
        note = get_note(id,request.user)
        obsolete_categories = request.POST.getlist('remove_categories')
        note = post_remove_categories(id,request.user, obsolete_categories)
        if note:
            return redirect('list_categories', id=note.id)
        else:
            messages.error(request, "Error not existing note")
            return redirect('home')

# Filters notes by selected category.
@method_decorator(login_required, name='dispatch')
class FilterCategoriesView(View):
    def get(self, request):
        category_id = request.GET.get('category_id')
        if category_id:
            filtered_categories = filter_notes_by_category(request.user, category_id )
        else:
            filtered_categories = get_all_notes(user = request.user)
        user_categories = filter_categories_by_user(request.user)
        return render(request, 'backend/home.html', {'notes': filtered_categories,'categories':user_categories})