from django.db import models
from user.models import User
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models. CASCADE,  related_name ='posts')
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"post by{self.author.username} - {self.created_at}"

    class Meta:
        ordering = ['-created_at']


# Create your models here.
