from Tutorial.models import Item
from django.http.response import HttpResponseRedirect
from django.shortcuts import render


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


def show_item_details(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, "details.html", {"item": item})
