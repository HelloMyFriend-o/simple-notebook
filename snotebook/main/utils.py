from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy

from .models import Notes


class DataMixin(LoginRequiredMixin):
    """
    Mixin that passes the keyword arguments received by
    get_context_data() as the template context and redirects
    to login page if user is not logged in.
    """
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtered_notes_by_user_id'] = Notes.objects.filter(user_id=self.request.user).order_by('-id')
        # Check if the object is passed
        if kwargs:
            if not self.is_user_valid():
                raise Http404
            else:
                context['note_slug'] = self.kwargs['note_slug']
        return context

    def is_user_valid(self):
        """
        Return ''True'' if the user is the author of the post he is requesting
        and ''False'' if note.
        """
        return self.object.user_id == self.request.user.id
