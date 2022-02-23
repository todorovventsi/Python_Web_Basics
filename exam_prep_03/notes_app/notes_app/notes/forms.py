from django import forms

from notes_app.notes.models import Profile, Note


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'image']


class ProfileDeleteForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'image']


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'image']


class NoteDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ['title', 'content', 'image']


