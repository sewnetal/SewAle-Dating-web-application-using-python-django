from django.conf.urls import include, url
from pages.views import *
from account.views import *
from ideas import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', profile_view),
]