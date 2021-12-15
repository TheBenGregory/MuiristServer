from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from muiristapi.views import register_user, login_user, user_profile, ParkView, SnippetView, ListView
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'parks', ParkView, 'park')
router.register(r'snippets', SnippetView, 'snippet')
router.register(r'lists', ListView, 'list')
urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('user_profile', user_profile),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

