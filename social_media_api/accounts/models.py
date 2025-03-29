<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    bio = models.TextField(_('bio'), blank=True)
    profile_picture = models.ImageField(
        _('profile picture'), 
        upload_to='profile_pics/', 
        blank=True, 
        null=True
    )
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='following'
    )

    def __str__(self):
        return self.username
=======
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
>>>>>>> 81ca2c6 (Initial commit to sync with GitHub)
