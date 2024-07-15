
from django.urls import path

from .views import CMSStoryViewSet, PublicStoryViewSet

urlpatterns_cms = [
    path('', CMSStoryViewSet.as_view({'get': 'list', 'post': 'create', 'patch': 'update', 'delete': 'destroy'}), name='cms-story-list'),
]

urlpatterns_public = [
    path('', PublicStoryViewSet.as_view({'get': 'list'}), name='public-story-list'),
]