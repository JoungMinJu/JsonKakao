from rest_framework import serializers
from .models import Recommend_history

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend_history
        fields = '__all__'