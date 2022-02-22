from django.shortcuts import render


def index(request):
    return render(request, 'home-with-profile.html')


def note_create(request):
    return render(request, 'note-create.html')


def note_edit(request):
    return render(request, 'note-edit.html')


def note_delete(request):
    return render(request, 'note-delete.html')


def note_details(request):
    return render(request, 'note-details.html')


def profile_details(request):
    return render(request, 'profile.html')
