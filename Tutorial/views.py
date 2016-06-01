import random

from Tutorial.models import Item
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView


def index(request):
    if request.user.is_authenticated():
        param = "?order"
        objects = Item.objects.all()
        if "order" in request.GET:
            objects = objects.order_by("random_value")
            param = None
        return render(request, "index.html", {"items": objects, "order": param})
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
    item.random_value = random.randint(0, 1000000)
    item.save()
    return HttpResponseRedirect("/")


def remove_item(request, item_id):
    db_item = get_object_or_404(Item, pk=item_id)
    db_item.delete()
    return HttpResponseRedirect("/")


class ItemView(DetailView):
    template_name = "details.html"
    model = Item
