from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User)
#
#     #additional classes
#
#     portfolio_site = models.URLField(blank=True)
#
#     profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    # date_joined = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.username
