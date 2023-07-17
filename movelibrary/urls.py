from . import views
from django.urls import path
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Landing.as_view(), name='home'),
    path('library/', views.Library.as_view(), name='library'),
    path('profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('search/', views.MovementSearch.as_view(), name='search_results'),
    path(
        'bookmark/<slug:slug>/',
        views.MovementBookmark.as_view(),
        name='movement_bookmark'
    ),
    path(
        'add1rm/<slug:slug>/',
        views.OneRepMaxRecords.as_view(),
        name='movement_1rm'
    ),
    path(
        '<slug:slug>/',
        views.MovementDetail.as_view(),
        name='movement_detail'
    ),
    path(
        'edit_one_rm/<slug:slug>/<record_id>/',
        views.edit_one_rm,
        name='edit_one_rm'
    ),
    path(
        'delete_one_rm/<slug:slug>/<record_id>/',
        views.delete_one_rm,
        name='delete_one_rm'
    ),
]
