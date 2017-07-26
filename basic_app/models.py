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
    def __str__(self):
        return self.user.username

class RecruitProfileInfo(models.Model):
    player_grad_year = models.IntegerField()
    player_first_name = models.CharField(max_length = 40)
    player_last_name = models.CharField(max_length = 40)
    player_position = models.CharField(max_length = 5)
    player_height = models.CharField(max_length = 5)
    player_weight = models.IntegerField()
    player_school = models.CharField(max_length = 40)
    player_state = models.CharField(max_length = 2)
    # player_phone = models.PhoneNumberField(blank = True)
    player_phone = models.CharField( max_length = 15, blank = True)
    player_twitter = models.CharField(max_length = 40, blank = True)

    def __str__(self):
        return self.user.username

class NationalRecruitList(models.Model):

    player_grad_year = models.IntegerField()
    player_rivals_rank = models.IntegerField()
    player_espn_rank = models.IntegerField()
    player_first_name = models.CharField(max_length = 40)
    player_last_name = models.CharField(max_length = 40)
    player_position = models.CharField(max_length = 5)
    player_school = models.CharField(max_length = 40)
    player_state = models.CharField(max_length = 2)
    player_height = models.CharField(max_length = 5)
    player_weight = models.IntegerField()
    player_potential_schools = models.CharField(max_length = 260)
