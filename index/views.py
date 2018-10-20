from django.shortcuts import render
from django.template import RequestContext
from .models import LoggedUser
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.

def logged(request):
  #collects the logged users  
  logged_users = LoggedUser.objects.all().order_by('username')
  context = {
      'logged_users':logged_users,
  }

  return render(request, 'index/index.html', context)
  
  
  #return render_to_response('index/index.html',
  #                          {'logged_users': logged_users},
  #                          context_instance=RequestContext(request))

@requires_csrf_token
def logged_count(request):
    logged_user_count = LoggedUser.objects.count()

    context = {
        'logged_user_count': logged_user_count,
    }

    return render(request, 'index/home.html', context)
