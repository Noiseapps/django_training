from Tutorial import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_item, name='add'),
    url(r'^remove/(?P<item_id>[0-9]+)$', views.remove_item, name='remove'),
    url(r'^details/(?P<item_id>[0-9]+)$', views.show_item_details, name='details'),
    url(r'^error$', views.not_authenticated, name='error')
]
