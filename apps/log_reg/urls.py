from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login-page$', views.login_page),
    url(r'^register-page$', views.register_page),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
]