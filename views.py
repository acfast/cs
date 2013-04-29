from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth

# Just for test, telling you the server is working.
def hello(request):
  return render_to_response('base.html', {})

# For test, showing information of the player, check if the player has logged 
# in.
def showPersonalInformation(request):
	if (request.user.is_authenticated()):
		return HttpResponse(request.user.username + ' ' + request.user.email)
	else:
		return HttpResponse("Not logged in!")

# Should by complete on android, just for test.
def login(request):
	return render_to_response('login.html', {}, 
			context_instance = RequestContext(request))

# Player log out, return None.
# It seems not so robust to return None anyhow, since we don't know if auth. 
# logout will fail.
def logout(request):
	auth.logout(request)
	return None

# Handler POST from client, verify the username and password. If it's a valid 
# account, active it, return None otherwise.
def verify_login(request):
	username = request.POST.get('username', None)
	password = request.POST.get('password', None)
	if username is None or password is None: # deal with invalid access
		return None 

	user = auth.authenticate(username = username, password = password)
	if user is not None and user.is_active:
		auth.login(request, user) 
		return HttpResponseRedirect(" ??? ") # TODO: what should I return here?
	else:
		return None # None for failure
