from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

# Create your views here.
@login_required
def note_list(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    notes = Note.objects.filter(user=request.user).order_by("-created")
    return render(request, "note/note_list.html", {"notes": notes, "form": form})
