from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('create/', views.create, name='create'),
    path('<int:note_id>', views.detail, name='note_id'),
    path('search/', views.search, name='search')
]