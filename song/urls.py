from django.urls import path

from .views import CMSSongViewSet, PublicSongViewSet

urlpatterns_cms = [
    path('', CMSSongViewSet.as_view({'get': 'list', 'post': 'create', 'patch': 'update', 'delete': 'destroy'}), name='cms-song-list'),
]

urlpatterns_public = [
    path('', PublicSongViewSet.as_view({'get': 'list'}), name='public-song-list'),
]