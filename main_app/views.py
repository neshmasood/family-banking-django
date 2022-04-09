from django.shortcuts import render
from django.views import View 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm



# django auth

def login_view(request):
    # if POST, then authenticate the user (submitting the username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else: # it was a get request so send the empty login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})




def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')




# Create your views here.
