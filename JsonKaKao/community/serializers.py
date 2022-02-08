from .models import Comment, Community,Like
from rest_framework import serializers

class CommunitySerializer(serializers.ModelSerializer):
    # views.py에서 user값을 넘겨줬으므로 받아야한다.
    writer = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Community
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
