from Login import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.login_form, name='index'),
    url(r'^logout$', views.logout_user, name='index'),
    url(r'^check_login$', views.check_login, name='index')
]
