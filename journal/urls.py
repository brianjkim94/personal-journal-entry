from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('entry/<int:pk>/', views.entry_detail, name='entry_detail'),
    path('entry/new/', views.entry_create, name='entry_create'),
    path('entry/<int:pk>/edit/', views.entry_edit, name='entry_edit'),
    path('entry/<int:pk>/delete/', views.entry_delete, name='entry_delete'),
    path('search/', views.search_by_date, name='search_by_date'),
    path('search_by_tag/', views.search_by_tag, name='search_by_tag'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
