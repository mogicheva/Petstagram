from django.shortcuts import render, redirect

from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import PetPhoto


def show_home(request):
    context = {
        'hide_additional_nav_items':True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    if not profile:
        return redirect('401')
    pet_photos = set(PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile))
    context = {
        'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)