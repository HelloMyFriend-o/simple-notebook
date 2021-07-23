from django import forms

from .models import Notes


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = {'title', 'content'}
