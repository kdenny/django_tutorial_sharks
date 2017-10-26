from rest_framework import serializers

from .models import Shark, Ping


class SharkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shark
        fields = ('name', 'pings',)
        depth = 1