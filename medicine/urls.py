from django.urls import path
from . import views

app_name = "medicine"

urlpatterns = [
    path('medicine/', views.medicine, name='medicine'),
]