from django.urls import path

from notes_app.notes.views import index, note_create, note_edit, note_delete, note_details, profile_details, \
    profile_create, profile_edit, profile_delete

urlpatterns = [
    path("", index, name='home page'),

    path("add/", note_create, name='create note'),
    path("edit/<int:pk>/", note_edit, name='edit note'),
    path("delete/<int:pk>/", note_delete, name='delete note'),
    path("details/<int:pk>/", note_details, name='note details'),

    path("profile/<int:pk>/", profile_details, name='profile details'),
    path("profile/create/", profile_create, name='create profile'),
    path("profile/edit/<int:pk>/", profile_edit, name='edit profile'),
    path("profile/delete/<int:pk>/", profile_delete, name='delete profile'),
]
