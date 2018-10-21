from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from .models import LoggedUser
from django.views.decorators.csrf import requires_csrf_token
from .forms import UpdateUserInfoForm
from django.contrib.auth.models import User

# Create your views here.

#collects the logged users
def logged(request):  
  logged_users = LoggedUser.objects.all().order_by('username')
  context = {
      'logged_users':logged_users,
  }

  return render(request, 'index/index.html', context)
  
  
  #return render_to_response('index/index.html',
  #                          {'logged_users': logged_users},
  #                          context_instance=RequestContext(request))

# outputs the number of logged users
@requires_csrf_token
def logged_count(request):
    logged_user_count = LoggedUser.objects.count()
    user_email = request.user.email

    context = {
        'logged_user_count': logged_user_count,
        'user_email': user_email,
    }

    return render(request, 'index/home.html', context)

# updates the user settings 
def user_settings(request):
    if request.method == 'POST':
        updateForm = UpdateUserInfoForm(request.POST, instance=request.user)

        if updateForm.is_valid():
            updateInfo = updateForm.save(commit=False)
            updateInfo.save()

    else:
        updateForm = UpdateUserInfoForm(instance=request.user)

    context = {
        'update_form': updateForm,
    }

    return render(request, 'index/settings.html', context)
    
