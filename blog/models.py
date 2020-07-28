from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    # each attribute is different fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # means if user is deleted delete its post as well

    def __str__(self):
        return "title: {} and author: {}".format(self.title, self.author)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

    
    
       

