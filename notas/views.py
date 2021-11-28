from django.shortcuts import render,redirect
from .models import Notes
# Create your views here.
def home(request):
    print(Notes.objects.all())
    return render(request, 'index.html', context={'notes': Notes.objects.all()})

def create(request):
    if request.method == "GET":
        return render(request, 'create.html')
    if request.method == "POST":
        title = request.POST['title']
        notes = request.POST['notes']
        note = Notes(title=title, description=notes)
        note.save()
        return redirect(home)

def delete(request, id):
    note = Notes.objects.get(id=id)
    note.delete()
    return redirect(home)

def edit(request, id):
    note = Notes.objects.get(id=id)
    print(note)
    if request.method == "GET":
        return render(request, 'edit.html', context={'note': note})
    if request.method == "POST":
        print(request.POST)
        title = request.POST['title']
        notes = request.POST['notes']
        note.title = title
        note.description = notes
        note.save()
        return redirect(home)