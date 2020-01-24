from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AuthUserManager
from django.db.models.signals import post_save

from django.db import models

# Create your models here.
class UserManager(AuthUserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('sex', 'm')
        return super().create_superuser(username, email, password, **extra_fields)

class User(AbstractUser):
   sex = models.CharField(
       max_length=1,
       choices = (
           ('f', 'female'),
           ('m', 'male'),
           ),
       verbose_name='성별')
   objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)

post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)