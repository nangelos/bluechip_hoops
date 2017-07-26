from django.contrib import admin
from basic_app.models import UserProfileInfo, RecruitProfileInfo, NationalRecruitList


# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(RecruitProfileInfo)
admin.site.register(NationalRecruitList)
