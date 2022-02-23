from django.shortcuts import render, redirect

from notes_app.notes.forms import ProfileCreateForm, NoteCreateForm, NoteDeleteForm, ProfileDeleteForm
from notes_app.notes.models import Profile, Note


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'notes': notes,
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def note_create(request):
    if request.method == "POST":
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = NoteCreateForm()

    context = {
        'no_add_note_link': True,
        'form': form,
    }

    return render(request, 'note-create.html', context)


def note_edit(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == "POST":
        form = NoteCreateForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = NoteCreateForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def note_delete(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == "POST":
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = NoteDeleteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note
    }

    return render(request, 'note-details.html', context)


def profile_create(request):
    if request.method == "POST":
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileCreateForm()

    context = {
        'no_profile': True,
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def profile_edit(request, pk):
    pass


def profile_delete(request, pk):
    profile = Profile.objects.get(pk=pk)
    notes = Note.objects.all()

    if request.method == "POST":
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            notes.delete()
            return redirect('home page')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profile-delete.html', context)


def profile_details(request, pk):
    profile = get_profile()
    notes = Note.objects.all()
    notes_count = len(notes)

    context = {
        'profile': profile,
        'notes_count': notes_count
    }

    return render(request, 'profile.html', context)
