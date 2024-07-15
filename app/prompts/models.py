from django.db import models
from taggit.managers import TaggableManager


class Prompt(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    prompt_text = models.TextField()
    categories = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
