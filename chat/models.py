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
class Account (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #img = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.user.username