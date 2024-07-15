"""
URL configuration for illumino_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from illumino_api import settings

from auth.urls import urlpatterns as auth_urlpatterns
from story.urls import urlpatterns_public as story_public_urlpatterns, urlpatterns_cms as story_cms_urlpatterns
from song.urls import urlpatterns_public as song_public_urlpatterns, urlpatterns_cms as song_cms_urlpatterns

urlpatterns = [
    path('api', include([
        path('/cms', include([
            path('/story', include([
                path('', include(story_cms_urlpatterns)),
            ])),
            path('/song', include([
                path('', include(song_cms_urlpatterns)),
            ])),
        ])),
        path('/auth', include([
            path('', include(auth_urlpatterns)),
        ])),
        path('/story', include([
            path('', include(story_public_urlpatterns)),
        ])),
        path('/song', include([
            path('', include(song_public_urlpatterns)),
        ])),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)