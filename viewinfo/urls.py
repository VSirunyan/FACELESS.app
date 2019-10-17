from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_wifis', views.get_wifis, name='get_wifis'),
]
