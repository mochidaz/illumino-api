from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = [
            'id', 'title', 'author', 'content', 'image', 
            'audio', 'reader_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
