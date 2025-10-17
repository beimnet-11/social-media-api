from rest_framework import serializers
from .models import Post, like, Comment
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
        model = like
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
        return obj.likes.count()
    def get_comments_count(self, obj):
        return obj.comments.count()
    def get_is_liked(self, obj):  
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['content']
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
                