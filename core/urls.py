from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send-newsletter/', views.send_newsletter, name='send_newsletter'),
]
