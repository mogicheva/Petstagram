from django.urls import path

from petstagram.main_app.views.generic import show_home, show_dashboard
from petstagram.main_app.views.pet_photos import show_pet_photo_details, add_photo, edit_photo, like_pet
from petstagram.main_app.views.pets import edit_pet, add_pet, delete_pet
from petstagram.main_app.views.profiles import show_profile, create_profile, profile_edit, profile_delete

urlpatterns = [
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', profile_edit, name='edit profile'),
    path('profile/delete/', profile_delete, name='delete profile'),

    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
    path('photo/add/', add_photo, name='add photo'),
    path('photo/edit/<int:id>/', edit_photo, name='edit photo'),
    path('photo/like/<int:pk>/', like_pet, name='like pet'),

    path('pet/edit/<int:pk>/', edit_pet, name ='pet edit'),
    path('pet/add/', add_pet, name='add pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='pet delete'),
]