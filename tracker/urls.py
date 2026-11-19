from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('signup/', views.signup, name='signup'),
    path('add/', views.add_application, name='add_application'),
    path('<int:pk>/edit/', views.edit_application, name='edit_application'),
    path('<int:pk>/delete/', views.delete_application, name='delete_application'),
    path('dashboard/', views.dashboard, name='dashboard'),
    ]
