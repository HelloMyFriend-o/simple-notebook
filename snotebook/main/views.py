from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.base import TemplateView

from .forms import AddNoteForm
from .models import Notes
from .utils import DataMixin


class NotesHome(DataMixin, TemplateView):
    """Displaying the main page."""
    template_name = 'main/home.html'


class CreateNote(DataMixin, CreateView):
    """Creating a new note."""
    form_class = AddNoteForm
    template_name = 'main/add_note.html'

    def get_form_kwargs(self):
        """Adding a user id to a note when it is created."""
        kwargs = super(CreateNote, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Notes()
        kwargs['instance'].user = self.request.user
        return kwargs


class ShowNote(DataMixin, DetailView):
    """Displaying the selected note."""
    model = Notes
    template_name = 'main/show_note.html'
    slug_url_kwarg = 'note_slug'


class UpdateNote(DataMixin, UpdateView):
    """Updating the selected note."""
    form_class = AddNoteForm
    template_name = 'main/add_note.html'

    def get_object(self, queryset=None):
        """Getting the object to update."""
        slug_ = self.kwargs.get('note_slug')
        return get_object_or_404(Notes, slug=slug_)


class DeleteNote(DataMixin, DeleteView):
    """Deleting the selected note."""
    form_class = AddNoteForm

    def get_object(self, queryset=None):
        """Getting the object to delete."""
        slug_ = self.kwargs.get('note_slug')
        return get_object_or_404(Notes, slug=slug_)

    def get_success_url(self):
        return reverse_lazy('home')


def page_note_found_view(request, exception):
    return render(request, 'main/404_not_found.html')
