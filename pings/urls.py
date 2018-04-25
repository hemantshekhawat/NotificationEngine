from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'notification/send/', views.send_notification, name='send_notification')
]