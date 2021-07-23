from django.contrib import admin

from .models import Notes


class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title', 'content')
    search_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Notes, NotesAdmin)
