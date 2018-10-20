from django.shortcuts import render
from django.template import RequestContext
from .models import LoggedUser

# Create your views here.

def logged(request):
  logged_users = LoggedUser.objects.all().order_by('username')
  context = {
      'logged_users':logged_users,
  }

  return render(request, 'index/index.html', context)
  
  
  #return render_to_response('index/index.html',
  #                          {'logged_users': logged_users},
  #                          context_instance=RequestContext(request))
