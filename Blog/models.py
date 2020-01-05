from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    pubdate = models.DateTimeField()
   # myimage = models.ImageField(upload_to='mages/', null=True)
    
    def pre(self):
        return self.text[:8]

    def __str__(self):
        return self.title
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,null=True)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    comment = models.TextField()
    pubdate = models.DateTimeField(default= timezone.now())
   # myimage = models.ImageField(upload_to='mages/', null=True)
    def __str__(self):
        return self.comment  