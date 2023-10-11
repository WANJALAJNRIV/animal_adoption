from django.urls import path
from . import views

urlpatterns = [
    # Public pet views
    path('petslist', views.public_pets_view, name="public_pets_view"),
    path('pet/<int:pet_id>/details', views.public_pet_detail, name='public_pet_detail'),

    # Staff pet views
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('pets/create/', views.pet_create, name='pet_create'),
    path('pets/<int:pet_id>/update/', views.pet_update, name='pet_update'),
    path('pets/<int:pet_id>/delete/', views.pet_delete, name='pet_delete'),

    # Search pets view
    path('search/', views.search_pets, name='search_pets'),
]
