from rest_framework import serializers

from journal.models import Journal
from user.serializers import UserSerializer


class JournalSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_id', read_only=True)

    class Meta:
        model = Journal
        fields = '__all__'