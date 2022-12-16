from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=24)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    fav_num = models.IntegerField(default=0)
    #img = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.title
    def post(self):
        self.created_at = timezone.now()  
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #img = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.username
    def post(self):
        self.created_at = timezone.now()
class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=24)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text[:20]
    def post(self):
        self.created_at = timezone.now()