from django.urls import path

from notes_app.notes.views import index, note_create, note_edit, note_delete, note_details, profile_details

urlpatterns = [
    path("", index, name='home page'),
    path("add/", note_create, name='create note'),
    path("edit/<int:id>/", note_edit, name='edit note'),
    path("delete/<int:id>/", note_delete, name='delete note'),
    path("details/<int:id>/", note_details, name='note details'),
    path("profile/", profile_details, name='profile details'),
]
