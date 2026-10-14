from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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