from django.shortcuts import render
from rest_framework import viewsets

from story.models import Story
from story.serializers import StorySerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def get_queryset(self):
        return Story.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()

    def get_serializer_class(self):
        if self.action == 'list':
            return StoryListSerializer
        return StorySerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), IsOwner()]

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)