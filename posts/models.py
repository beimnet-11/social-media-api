from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,  related_name ='posts')
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"post by {self.author.username} - {self.created_at}"

    class Meta:
        ordering = ['-created_at']
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models. CASCADE, related_name='Likes')
    post=models.ForeignKey(Post,on_delete=models. CASCADE, related_name='Likes')
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} likes post {self.post.id}"


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='comments')
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on post {self.post.id}"

    class Meta:
        ordering = ['-created_at']
    


# Create your models here.
