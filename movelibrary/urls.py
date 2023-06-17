from . import views
from django.urls import path

urlpatterns = [
    path('', views.Landing.as_view(), name='home'),
    # path('accounts/login/', allauth_views.LoginView.as_view(), name='login'),
]
