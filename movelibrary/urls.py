from . import views
from django.urls import path

urlpatterns = [
    path('', views.Landing.as_view(), name='home'),
    path('search/', views.MovementSearch.as_view(), name='search_results'),
    path(
        '<slug:slug>/', views.MovementDetail.as_view(), name='movement_detail'
    ),
    # path('accounts/login/', allauth_views.LoginView.as_view(), name='login'),
]
