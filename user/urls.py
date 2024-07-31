from django.urls import path

from user.views import UserProfileViewSet

urlpatterns_public = [
    path('/profile', UserProfileViewSet.as_view({
        'get': 'retrieve',
    }), name='public-user-list'),
]