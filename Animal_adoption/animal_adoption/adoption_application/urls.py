# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('apply/<int:pet_id>/', views.apply_for_adoption, name='apply_for_adoption'),
    path('approve/<int:application_id>/', views.approve_application, name='approve_application'),
    path('reject/<int:application_id>/', views.reject_application, name='reject_application'),
    path('applications/', views.adoption_application_list, name='adoption_application_list'),
    path('applications/<int:application_id>/', views.adoption_application_detail, name='adoption_application_detail'),

    path('applications/my/<int:application_id>/', views.public_application_detail, name='public_adoption_application_detail'),



]
