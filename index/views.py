from django.shortcuts import render
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

    context = {
        'logged_user_count': logged_user_count,
    }

    return render(request, 'index/home.html', context)

# updates the user settings //needs fixing
def user_settings(request):
    if request.method == 'POST':
        updateForm = UpdateUserInfoForm(request.POST)
        User.objects.get(username=LoggedUser.username).update(email=request.POST['new_email'])

    else:
        updateForm = UpdateUserInfoForm()

    context = {
        'update_form': updateForm,
    }

    return render(request, 'index/settings.html', context)
    
