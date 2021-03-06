from django.shortcuts import render
from django.views.generic import View



class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/index.html", {})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/login.html", {})

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/register.html", {})

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/profiles.html", {})

class SingleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/single.html", {})
class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/contact.html", {})
class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "web/about.html", {})


