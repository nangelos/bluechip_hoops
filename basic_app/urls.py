from django.conf.urls import url
from basic_app import views

# TEMPLATE URLs
app_name = 'basic_app'

urlpatterns =[
    url(r'^$', views.index, name = 'index'),
    url(r'^info/', views.info, name = 'info'),
    url(r'^signup/', views.register, name = 'signup'),
    url(r'^news/', views.news, name = 'news'),
    url(r'^national_rankings/', views.natl_rank, name = 'natl_rank'),
    url(r'^my_recruits/', views.my_recruits, name = 'my_recruits'),
    url(r'^upcoming_events/', views.upcoming, name = 'upcoming'),
    url(r'^manage_staff/', views.manage_staff, name = 'manage_staff'),
    url(r'^social_media/', views.manage_social, name = 'manage_social'),
    url(r'^login/', views.user_login, name = 'login'),
]
