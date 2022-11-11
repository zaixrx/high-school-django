from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):  
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/images', blank=True)