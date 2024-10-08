from django.db import models

from song.models import Song


class Story(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='story/', null=True, blank=True)
    audio = models.FileField(upload_to='story/', null=True, blank=True)
    reader_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title