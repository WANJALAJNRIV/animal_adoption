# Import the required modules and views
from django.urls import path
from . import views

# Define the URL patterns for your app
urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # User authentication URLs
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),

    # User profile
    path('profile/', views.profile, name='profile'),

    # User management URLs
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/update/<int:pk>/', views.user_update, name='user_update'),
    path('users/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),

    # User and staff dashboards
    path('mydashboard/', views.user_dashboard, name='user_dashboard'),
    path('dashboard/', views.staff_dashboard, name='staff_dashboard'),
]
