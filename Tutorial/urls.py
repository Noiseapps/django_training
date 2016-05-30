from Tutorial import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout$', views.logout_user, name='index'),
    url(r'^login$', views.login_form, name='index'),
    url(r'^check_login$', views.check_login, name='index'),
    url(r'^add$', views.add_item, name='index'),
    url(r'^remove/(?P<item_id>[0-9]+)$', views.remove_item, name='index'),
    url(r'^error$', views.not_authenticated, name='index')
]