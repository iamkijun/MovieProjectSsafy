from community.models import Comment
from rest_framework import serializers
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)


class CommentListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username',)

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'content', 'user', 'created_at', 'updated_at')
