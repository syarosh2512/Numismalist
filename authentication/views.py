from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from authentication.forms import LoginForm


# Create your views here.
def login_user(request):
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'login_form': LoginForm(),
                    'attention': f'The user with username = <{username}> and password were not find '
                }
        else:
            context = {
                'login_form': LoginForm()
            }

    return render(request, 'auth/login.html', context)


def register_user(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('index')
    context = {'form': form}
    return render(request, 'auth/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')
