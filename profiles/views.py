from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, UserUpdateForm


def profile(request):
    """display user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        userForm = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid() and userForm.is_valid():
            profile = form.save(commit=False)
            user = userForm.save()
            profile.user = user

            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            profile.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
        userForm = UserUpdateForm(instance=request.user)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
        'userForm': userForm,
        'on_profile_page': True,
    }

    return render(request, template, context)


def update_profile(request):
    """update user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        userForm = UserUpdateForm(request.POST,
                                  instance=request.user)
        if form.is_valid() and userForm.is_valid():
            form.save()
            userForm.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
        userForm = UserUpdateForm(instance=request.user)

    template = 'profiles/update_profile.html'
    context = {
        'form': form,
        'userForm': userForm,
        'on_profile_page': True,
    }

    return render(request, template, context)
