from . import views
from django.urls import path

urlpatterns = [
    path('', views.Landing.as_view(), name='home'),
    path('search/', views.MovementSearch.as_view(), name='search_results'),
    path(
        'bookmarks/',
        views.BookmarksList.as_view(),
        name='bookmarks_list'
    ),
    path(
        '<slug:slug>/',
        views.MovementDetail.as_view(),
        name='movement_detail'
    ),
    path(
        'bookmark/<slug:slug>/',
        views.MovementBookmark.as_view(),
        name='movement_bookmark'
    ),
    # path('accounts/login/', allauth_views.LoginView.as_view(), name='login'),
]
