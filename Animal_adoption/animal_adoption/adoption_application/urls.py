# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...

    path('apply/<int:pet_id>/', views.apply_for_adoption, name='apply_for_adoption',
         name='apply_for_adoption'),
    # Allows users to apply for pet adoption.

    path('approve/<int:application_id>/', views.approve_application, name='approve_application',
         name='approve_application'),
    # Allows application managers and administrators to approve an adoption application.

    path('reject/<int:application_id>/', views.reject_application, name='reject_application',
         name='reject_application'),
    # Allows application managers and administrators to reject an adoption application.

    path('applications/', views.adoption_application_list, name='adoption_application_list',
         name='adoption_application_list'),
    # Lists pending adoption applications for review.

    path('applications/<int:application_id>/', views.adoption_application_detail,
         name='adoption_application_detail'),
    # Displays detailed information about a specific adoption application.

    path('applications/my/<int:application_id>/', views.public_application_detail,
         name='public_adoption_application_detail'),
    # Allows users to view details of their own adoption applications.

    path('applications_pet/<int:pet_id>/', views.pet_adoption_applications,
         name='pet_adoption_applications'),
    # Lists pending adoption applications for a specific pet owner to review.
]
