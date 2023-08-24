from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import NotesForm, CreateUserForm
from .models import Notes, Trash

# Create your views here.

@login_required(login_url='notesapp:login')
def home_view(request):
    return render(request, 'notesapp/home.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('notesapp:notes')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ username)

                return redirect('notesapp:login')
        
    context = {'form' : form}
    return render(request, 'notesapp/signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('notesapp:notes')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('notesapp:notes')
            else:
                messages.error(request, 'Invalid Username or Password')

        return render(request, 'notesapp/login.html')
    

def logout_view(request):
    logout(request)
    return redirect('notesapp:login')



@login_required(login_url='notesapp:login')
def create_note(request):
    form = NotesForm(request=request)
    if request.method == 'POST':
        form = NotesForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('notesapp:notes')
        else:
            print('Error')

    context={
        'form':form,
    }

    return render(request, 'notesapp/addnote.html', context)


@login_required(login_url='notesapp:login')
def list_notes_view(request):
    notes_list = Notes.objects.filter(user=request.user)
    context = {
        'notes_list' : notes_list,
    }
    
    return render(request, 'notesapp/notes.html', context)


@login_required(login_url='notesapp:login')
def update_note(request, id):
    item = Notes.objects.filter(user=request.user).get(id=id)
    form = NotesForm(request.POST or None, instance=item, request=request)
    if form.is_valid():
        form.save()
        return redirect('notesapp:notes')

    return render(request, 'notesapp/update_note.html', {'form':form})
    

@login_required(login_url='notesapp:login')
def trash_view(request):
    trash_list = Trash.objects.filter(user=request.user)
    context = {
        'trash_list' : trash_list,
    }
    
    return render(request, 'notesapp/trash.html', context)


@login_required(login_url='notesapp:login')
def delete_trash(request, id):
    item = Trash.objects.filter(user=request.user).get(id=id)
    if item:
        item.delete()
        return redirect('notesapp:trash')
    return render(request, 'notesapp/trash.html')


@login_required(login_url='notesapp:login')
def move_to_trash(request, id):
    item = Notes.objects.filter(user=request.user).get(id=id)
    if item:
        trash_entry = Trash.objects.create(title=item.title, content=item.content, user=request.user)
        trash_entry.save()
        item.delete()
    return redirect('notesapp:notes')



def handling_404(request, exception):
    return render(request, 'notesapp/404.html', status=404)