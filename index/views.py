from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from .models import LoggedUser, Profile, Alerts
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UpdateUserInfoForm, UpdateUserProfileForm, AlertsForm
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User

# Create your views here.

#collects the logged users
def logged(request):  
  logged_users = LoggedUser.objects.all().order_by('username')
  context = {
      'logged_users':logged_users,
  }

  return render(request, 'index/index.html', context)
  
# outputs the number of logged users
@requires_csrf_token
def logged_count(request):
    logged_user_count = LoggedUser.objects.count()
    user_email = request.user.email
    user_profile = Profile.objects.get(user_id=request.user.id)
    alerts_on = Alerts.objects.count()

    context = {
        'logged_user_count': logged_user_count,
        'user_email': user_email,
        'user_profile':user_profile,
        'alerts_on':alerts_on,
    }

    return render(request, 'index/home.html', context)

# updates the user settings 
@login_required
@transaction.atomic
def user_settings(request):
    if request.method == 'POST':
        updateForm = UpdateUserInfoForm(request.POST, instance=request.user)
        profileForm = UpdateUserProfileForm(request.POST, instance=request.user.profile)

        # checks if the update form and profile form, the extension for User models, is valid
        if updateForm.is_valid() and profileForm.is_valid():
            updateInfo = updateForm.save(commit=False)
            profileInfo = profileForm.save(commit=False)
            updateInfo.save()
            profileInfo.save()

    else:
        updateForm = UpdateUserInfoForm(instance=request.user)
        profileForm = UpdateUserProfileForm(instance=request.user.profile)

    context = {
        'update_form': updateForm,
        'profile_form': profileForm,
    }

    return render(request, 'index/settings.html', context)

# posts alerts if the user is an admin
@user_passes_test(lambda u: u.is_staff)
def post_alert(request):
    alert_form = AlertsForm(request.POST or None)
    if alert_form.is_valid():
        alert_post = alert_form.save(commit=False)
        alert_post.user = request.user
        alert_post.save()
    
    context = {
        'alert_form': alert_form,
    }

    return render(request, 'index/admin.html', context)

# lists all the alerts present within the alert page
@user_passes_test(lambda u: u.is_staff)
def list_alert(request):
    alerts_list = Alerts.objects.all().order_by("-publish_date")

    context = {
        'alerts_list':alerts_list,
    }

    return render(request, 'index/systemalerts.html', context)

# shows the details of the alert
@user_passes_test(lambda u: u.is_staff)
def view_alert(request, slug):
    posted_alert = get_object_or_404(Alerts, slug=slug)
    context = {
        'posted_alert': posted_alert,
    }
    return render(request, 'index/alertsdetails.html', context)
    
