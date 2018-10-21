from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from .models import LoggedUser, Profile
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserInfoForm, UpdateUserProfileForm
from django.contrib import messages
from django.db import transaction

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

    context = {
        'logged_user_count': logged_user_count,
        'user_email': user_email,
        'user_profile':user_profile,
    }

    return render(request, 'index/home.html', context)

# updates the user settings 
@login_required
@transaction.atomic
def user_settings(request):
    if request.method == 'POST':
        updateForm = UpdateUserInfoForm(request.POST, instance=request.user)
        profileForm = UpdateUserProfileForm(request.POST, instance=request.user.profile)

        if updateForm.is_valid():
            updateInfo = updateForm.save(commit=False)
            profileInfo = profileForm.save(commit=False)
            updateInfo.save()
            profileInfo.save()

            messages.success(request, "Your profile was successfully updated!")
        
        else:
            messages.error(request, "Please correct the error below.")

    else:
        updateForm = UpdateUserInfoForm(instance=request.user)
        profileForm = UpdateUserProfileForm(instance=request.user.profile)

    context = {
        'update_form': updateForm,
        'profile_form': profileForm,
    }

    return render(request, 'index/settings.html', context)
    
