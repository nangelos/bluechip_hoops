from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo, RecruitProfileInfo, NationalRecruitList

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        # fields = ('username','email', 'password')
        fields = ('email', 'password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('first_name', 'last_name')

class RecruitProfileInfoForm(forms.ModelForm):
    class Meta():
        model = RecruitProfileInfo
        fields = ('player_grad_year', 'player_first_name', 'player_last_name',
        'player_position', 'player_height', 'player_weight', 'player_school',
        'player_state', 'player_phone', 'player_twitter')
