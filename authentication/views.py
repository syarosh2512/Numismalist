from django.contrib.auth import logout
from django.shortcuts import render, redirect
from authentication.forms import LoginForm

# Create your views here.
def login_user(request):
    context = {'login_form': LoginForm()}
    return render(request, 'auth/my_oldlogin.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')
