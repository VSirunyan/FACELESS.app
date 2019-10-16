from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getInfo', views.getInfo, name='getInfo'),
]
