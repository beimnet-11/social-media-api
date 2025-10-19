from rest_framework import serializers
from .models import Post, Like, Comment
from user.serializers import UserRegistrationSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer(read_only=True)
    class Meta:
        model = Like
        fields = ['id', 'user', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    author = UserRegistrationSerializer(read_only=True)
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'like_count', 'is_liked', 'comments']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at', 'like_count', 'is_liked', 'comments']
    
    def get_like_count(self, obj):
        return 0  # Temporary fix - returns 0 likes
    
    def get_is_liked(self, obj):  
        return False  # Temporary fix - returns False for is_liked

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']