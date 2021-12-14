from rest_framework import serializers
from .models import Poll



class PollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Poll