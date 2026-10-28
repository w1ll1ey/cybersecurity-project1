from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

# FLAW 5: SECURITY LOGGING AND MONITORING FAILURES (A09, 2021) (missing logging of failed logins)

# FIX 5: uncomment the code below and FIX 5 block in settings.py to create a logger for failed logins

# from django.contrib.auth.signals import user_login_failed
# from django.dispatch import receiver
# from logging import getLogger

# logger = getLogger("security")

# @receiver(user_login_failed)
# def security_logger(sender, credentials, request, **kwargs):
#     if request:
#         logger.warning(f"Failed login for user {credentials.get('username')} from {request.META.get('REMOTE_ADDR')}")
#     else:
#         logger.warning(f"Failed login for user {credentials.get('username')} from unknown")

@login_required
def notes(request):
    context = Note.objects.filter(creator=request.user)
    return render(request, "notes/note_list.html", {"notes": context})

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

# FLAW 1: BROKEN ACCESS CONTROL (A01, 2021)

@login_required
def detail(request, note_id):
   note = get_object_or_404(Note, id=note_id)
   return render(request, "notes/detail.html", {"note": note})

# FIX 1: FILTER BY CREATOR

# @login_required
# def detail(request, note_id):
#    note = get_object_or_404(Note, creator=request.user, id=note_id)
#    return render(request, "notes/detail.html", {"note": note})

# FLAW 3: INJECTION (A03, 2021)

@login_required
def search(request):
    results = []
    query = request.GET.get("q", "")
    if query:
        results = Note.objects.raw(f"SELECT * FROM notes_note WHERE creator_id = {request.user.id} AND NAME LIKE '%%{query}%%'")
    return render(request, "notes/search.html", {"notes": results, "query": query})

# FIX 3: DON'T BYPASS DJANGO'S ORM

# @login_required
# def search(request):
#     results = []
#     query = request.GET.get("q", "")
#     if query:
#         results = Note.objects.filter(creator=request.user, name__icontains=query)
#     return render(request, "notes/search.html", {"notes": results, "query": query})

@login_required
def delete(request, note_id):
    if request.method == "POST":
        note = get_object_or_404(Note, creator=request.user, id=note_id)
        note.delete()
    return redirect("notes")