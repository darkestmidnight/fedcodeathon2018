from django.db import models
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
  
# class to keep track of the currently logged in users
class LoggedUser(models.Model):
  username = models.CharField(max_length=30, primary_key=True)
  
  def __unicode__(self):
    return self.username

def login_user(sender, request, user, **kwargs):
  LoggedUser(username=user.username).save()

def logout_user(sender, request, user, **kwargs):
  try:
    u = LoggedUser.objects.get(pk=user.username)
    u.delete()
  except LoggedUser.DoesNotExist:
    pass
    
user_logged_in.connect(login_user)
user_logged_out.connect(logout_user)

# This class is to extend the default user model provided by django
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emergency_contact = models.CharField(max_length=100, blank=True)
    office_location = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)

# signals to automatically  create Profile when user_info is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# signals to automatically update Profile when user_info is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()