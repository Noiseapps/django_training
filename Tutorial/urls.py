from Tutorial import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_item, name='add'),
    url(r'^delete/(?P<item_id>[0-9]+)$', views.remove_item, name='remove'),
    url(r'^details/(?P<pk>[0-9]+)$', views.ItemView.as_view(), name='details'),
    url(r'^error$', views.not_authenticated, name='error')
]
