from . import views
from django.urls import path

urlpatterns = [
    path('', views.LastMovement.as_view(), name='home')
]