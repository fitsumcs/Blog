from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(default = "This is Default Text")
    pubdate = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.title
    