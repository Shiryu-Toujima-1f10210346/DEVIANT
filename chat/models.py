from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    looks = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    fav_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    #img = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.title
    def post(self):
        self.created_at = timezone.now()  

class Comment(models.Model):
    post_comment_id = models.IntegerField(default=1)
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=24)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text[:20]
    def post(self):
        self.created_at = timezone.now()
#自分がお気に入りした投稿を保存するモデル
class FavoriteList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.post.title