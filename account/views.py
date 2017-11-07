from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from account.models import UserProfile, User
from django.contrib.auth.decorators import login_required
from datetime import date


from django.contrib.auth.forms import UserCreationForm




def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect("index.html")
    return render(request,"web/login.html")

def register_view(request):
    form2 = UserRegistrationForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None, request.FILES or None)
    if form2.is_valid() and profile_form.is_valid():
        user = form2.save()
        password = form2.cleaned_data.get('password')
        email    = form2.cleaned_data.get('email')
        user.first_name = form2.cleaned_data.get('firstname')
        user.last_name = form2.cleaned_data.get('lastname')
        user.set_password(password)
        user.username = email
        user.save()
        profile = profile_form.save(commit= False)
        profile.user = user
        profile.bio = profile_form.cleaned_data.get('bio')
        profile.country = profile_form.cleaned_data.get('country')
        profile.gender = request.POST.get('gender')
        profile.DOB = request.POST.get('DOB')
        print(profile.DOB)
        if 'photo' in request.FILES:
            profile.photo = request.FILES ['photo']
        elif profile.gender == 'male':
            profile.photo = 'profile_images/profile-default-male.png'
        elif profile.gender == 'female':
            profile.photo = 'profile_images/user_profile_female.jpg'
        profile.save()
        #login(request,user)
        return HttpResponseRedirect("login.html")

    return render(request, "web/register.html",{"form1": form2, 'profile_form': profile_form})
def logout_view(request):
    logout(request)
    return render(request,"web/index.html")

@login_required(login_url='/login.html')
def profile_view(request,pk):
    data = User.objects.all()
    user_profile = User.objects.get(pk = pk)
    photo_photo = user_profile.user.photo.url
    return render(request,'web/single.html', {'photo_test': photo_photo,'user_profile': user_profile,'all_user':data,
                                               })

def home_view(request):
    data = User.objects.all()
    return render(request,'web/index.html', {'all_user':data,})










