from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def home(request):
  return render(request, 'main/search.html')



def search_profile(request):
    if 'username' in request.GET and request.GET['username']:
        name = request.GET.get("username")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'main/results.html', params)
    else:
        message = "You haven't searched for a Profile"
    return render(request, 'main/results.html', {'message': message})
