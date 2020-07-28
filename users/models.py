from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # cascade means if a user is deleted, then also delete the profile
    # but if we delete the profile, it won't delete the user

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
                



        




"""
Now that we have added this model
  Remember that any time we make a change to our models, this is also gona make a change to the database.
  But it hasn't made any changes yet
  we still need to run our migrations for those changes to take effect
  and that is also a great thing about migrations
  because we can make database changes like this over time
  so lets bring our terminal and run our migrations

1- python manage.py makemigrations
        on executing command 1 we will get an arror "pip install Pillow"
        Pillow is a library of working with images within python

2- pip install Pillow

3- python manage.py makemigrations

            it created a new migrations file for us, inside     'users/migrations/0001_initial.py'

4- python manage.py migrate

                sucessful update to database

So, now i wana be able to view these user profiles on the admin page of our website
so that we can see how this looks like
but, if i want to do this, then we have to remember we need to register this model with in the admin file
of our app             "this is a easy step to forget"

open users -> admin.py file

                        from django.contrib import admin
                        from .models import Profile

                        # Register your models here.
                        # we will register our Profile model here that we have created

                        admin.site.register(Profile)

"""

