from django.urls import path
from . import views

app_name = "online_buy"

urlpatterns = [
    path('online_buy/', views.online_buy, name='online_buy')
]