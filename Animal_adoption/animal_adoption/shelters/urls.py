# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('shelters/', views.shelter_list, name='shelter_list'),
    path('shelters/<int:shelter_id>/', views.shelter_detail, name='shelter_detail'),
    path('shelters/create/', views.shelter_create, name='shelter_create'),
    path('shelters/<int:shelter_id>/update/', views.shelter_update, name='shelter_update'),
    path('shelters/<int:shelter_id>/delete/', views.shelter_delete, name='shelter_delete'),
]
