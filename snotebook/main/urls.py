from django.urls import path

from .views import *

urlpatterns = [
    path('', NotesHome.as_view(), name='home'),
    path('add_note/', CreateNote.as_view(), name='add_note'),
    path('note/<slug:note_slug>/', ShowNote.as_view(), name='show_note'),
    path('note/<slug:note_slug>/update_note/', UpdateNote.as_view(), name='update_note'),
    path('note/<slug:note_slug>/delete_note/', DeleteNote.as_view(), name='delete_note')
]
