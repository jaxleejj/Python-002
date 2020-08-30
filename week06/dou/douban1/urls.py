from django.urls import path
from . import views


urlpatterns = [
    path('douban', views.show_page),
    path('', views.index),
]