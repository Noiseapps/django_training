from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import MyLoginForm
from django.contrib.auth import authenticate, login, logout


def check_login(request):
    if request.method == "POST":
        form = MyLoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    form.add_error(None, ValidationError("User is deactivated"))
            else:
                form.add_error(None, ValidationError("Username and passwords do not match"))
        return render(request, "login.html", {"form": form})
    return HttpResponseRedirect("/error")


def login_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == "POST":
        return check_login(request)
    else:
        form = MyLoginForm()
        return render(request, "login.html", {"form": form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
