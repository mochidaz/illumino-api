from rest_framework import serializers

from song.models import Genre, Song


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(source='genre_id', read_only=True)
    class Meta:
        model = Song
        fields = '__all__'