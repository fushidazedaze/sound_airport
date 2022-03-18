from time import time
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

title_length = 15

places = (
    ('city', 'City'),
    ('forest', 'Forest'),
    ('sea', 'Sea'),
    ('planet', 'Planet')
)


class User(AbstractUser):
    pass


class Post(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    icon = models.SlugField(choices=places)
    title = models.CharField(max_length=title_length, default='No Title')
    sound = models.FileField(upload_to='',)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
