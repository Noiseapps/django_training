import random

from Tutorial.models import Item
from django.contrib.auth.decorators import login_required, permission_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def not_authenticated(request):
    return render(request, template_name="error.html")


@login_required(login_url="/login/")
@permission_required("Tutorial.add_item", raise_exception=True)
def add_item(request):
    objects = Item.objects.all().order_by("id")
    if objects:
        item = Item(name="Object %d" % (objects.last().id + 1))
    else:
        item = Item(name="Object 0")
    item.random_value = random.randint(0, 1000000)
    item.save()
    return HttpResponseRedirect("/")


@login_required(login_url="/login/")
@permission_required("Tutorial.delete_item")
def remove_item(request, item_id):
    print(request.user.get_all_permissions())
    db_item = get_object_or_404(Item, pk=item_id)
    db_item.delete()
    return HttpResponseRedirect("/")


class ItemView(DetailView):
    template_name = "details.html"
    model = Item
