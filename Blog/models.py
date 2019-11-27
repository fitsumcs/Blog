from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    pubdate = models.DateTimeField()
    def pre(self):
        return self.text[:8]

    def __str__(self):
        return self.title
    