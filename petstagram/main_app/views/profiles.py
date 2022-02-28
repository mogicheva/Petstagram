from django.shortcuts import render, redirect

from petstagram.main_app.forms import ProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import Pet, PetPhoto


def show_profile(request):
    profile = get_profile()
    pets = list(Pet.objects.filter(user_profile=profile))
    pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
    total_likes_count = sum(pp.likes for pp in pet_photos)
    total_images_count = len(pet_photos)
    context = {
        'profile': profile,
        'total_likes_count': total_likes_count,
        'total_images_count': total_images_count,
        'pets': pets,
    }
    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm
    context = {
        'form': form,
    }
    return render(request, 'profile_create.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }

    return render(request, 'profile_edit.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile_delete.html', context)