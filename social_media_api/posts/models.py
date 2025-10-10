from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('accounts.CustomUser', related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.CustomUser', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'


class Like(models.Model):
    post = models.ForeignKey(post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(post, related_name='likes', on_delete=models.CASCADE)