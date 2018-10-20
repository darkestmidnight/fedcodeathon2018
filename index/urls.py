from django.urls import re_path, include
from . import views

app_name='logged_count'

# pages for the webapp.
urlpatterns = [
    re_path(r'^logcount', views.logged_count, name="logged_count"),
    re_path(r'^logusers$', views.logged, name="logged_users"),
]