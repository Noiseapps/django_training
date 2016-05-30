from Tutorial.models import Item
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    if request.user.is_authenticated():
        objects = Item.objects.all()
        return render(request, "index.html", {"items": objects})
    else:
        return HttpResponseRedirect("/error")


def not_authenticated(request):
    return render(request, template_name="error.html")


def add_item(request):
    objects = Item.objects.all().order_by("id")
    if objects:
        item = Item(name="Object %d" % (objects.last().id + 1))
    else:
        item = Item(name="Object 0")
    item.save()
    return HttpResponseRedirect("/")


def remove_item(request, item_id):
    Item.objects.get(pk=item_id).delete()
    return HttpResponseRedirect("/")


def check_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return HttpResponseRedirect("/")
    return HttpResponseRedirect("/error")


def login_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    return render(request, "login.html")
