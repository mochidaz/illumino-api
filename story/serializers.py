from rest_framework import serializers

from song.serializers import SongSerializer
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'