"""ideas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ideas import settings
from django.conf.urls.static import static
from django.views.static import serve
from pages.views import *
from account.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^user/', include('account.urls')),
    #url(r'^$', HomeView.as_view(), name='home'),
    url(r'^index.html', home_view, name='register'),
    url(r'^$', home_view, name='home'),
    url(r'^login.html', login_view, name = 'login'),
    url(r'^logout', logout_view, name = 'logout'),
    url(r'^register.html', register_view, name='register'),
    #url(r'^login.html', LoginView.as_view(), name = 'login'),
    #url(r'^register.html', RegisterView.as_view(), name='register'),
    url(r'^profiles.html', ProfileView.as_view(), name='profiles'),
    url(r'^single/(?P<pk>[a-zA-Z0-9]+)$', profile_view, name='single'),
    url(r'^contact.html', ContactView.as_view(), name='contact'),
    url(r'^about.html', AboutView.as_view(), name='about'),
    url(r'^admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

