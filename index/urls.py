from django.urls import re_path, include
from . import views

app_name='logged_count'

# pages for the webapp.
urlpatterns = [
    re_path(r'^$', views.logged_count, name="logged_count"),
    re_path(r'^loggedusers/', views.logged, name="logged_users"),
    re_path(r'^settings/', views.user_settings, name="update_info"),
]