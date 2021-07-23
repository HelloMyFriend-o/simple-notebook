from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Notes(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема')
    content = models.TextField(verbose_name='Содержание')
    slug = AutoSlugField(populate_from='title', unique=True, verbose_name='URL')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_note', kwargs={'note_slug': self.slug})

    class Meta:
        verbose_name = 'Записка'
        verbose_name_plural = 'Записки'
        ordering = ['title']
