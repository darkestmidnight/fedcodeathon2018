from django.urls import re_path, include
from . import views

app_name='logged'

# pages for the webapp.
urlpatterns = [
    re_path(r'^$', views.logged_count, name="logged_count"),
    re_path(r'^loggedusers/', views.logged, name="logged_users"),
    re_path(r'^settings/', views.user_settings, name="update_info"),
    re_path(r'^administrators/', views.post_alert, name="post_alert"),
    re_path(r'^alerts/$', views.list_alert, name="list_alert"),
    re_path(r'^alerts/(?P<slug>[\w-]+)/$', views.view_alert, name="view_alert"),
]