from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        note = Note()
        note.title = title
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all().last()
        return render(request, 'notes/index.html', {'notes': all_notes})