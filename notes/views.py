from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

def notes(request):
    
    return render(request, "notes/note_list.html", {})

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect("notes")
        else:
            return render(request, "registration/registration.html", {"form": form})
            
    form = UserCreationForm()
    return render(request, "registration/registration.html", {"form": form})

@login_required
def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.creator = request.user
            note.save()
            return redirect("notes")
    else:
        form = NoteForm()
    return render(request, "notes/create.html", {"form": form})