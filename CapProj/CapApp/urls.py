from django.conf.urls import url
from CapApp import views

urlpatterns = [
    url(r'^$', views.grants, name='grants'),
]
