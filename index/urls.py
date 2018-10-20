from django.urls import re_path, include
from . import views


# pages for the webapp.
urlpatterns = [
    re_path(r'^$', views.logged, name="logged_users"),
]