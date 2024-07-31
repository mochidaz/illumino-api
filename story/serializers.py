from rest_framework import serializers

from song.serializers import SongSerializer
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    audio = SongSerializer(source='audio_id', read_only=True)
    class Meta:
        model = Story
        fields = '__all__'