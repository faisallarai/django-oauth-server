import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider.decorators import protected_resource

from accounts.forms import SignUpForm

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    context = {
        "form": form
    }
    return render(request, 'accounts/signup.html', context)


@protected_resource(scopes=['read'])
def profile(request):
    print('request-faisal', request)
    raw = {
        "id": request.resource_owner.id,
        "username": request.resource_owner.username,
        "email": request.resource_owner.email,
        "first_name": request.resource_owner.first_name,
        "last_name": request.resource_owner.last_name
    }
    data = json.dumps(raw)
    return HttpResponse(data, content_type="application/json")

class ProfileEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        raw = {
            "id": request.resource_owner.id,
            "username": request.resource_owner.username,
            "email": request.resource_owner.email,
            "first_name": request.resource_owner.first_name,
            "last_name": request.resource_owner.last_name
        }

        data = json.dumps(raw)

        return HttpResponse(json, content_type="application/json")