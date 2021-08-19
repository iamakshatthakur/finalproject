from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.timezone import now
from django.contrib.auth.models import User,auth
from django.urls import reverse

# Create your models here.
class categorylist(models.Model):
    name= models.CharField(max_length=50,unique=True)
    img= models.ImageField(upload_to='categorylist',blank=True)
    slug=models.SlugField(unique=True)

    class  Meta:
        ordering=('name',)

    def __str__(self):
        return self.name


    
class Item(models.Model):
    sno=models.AutoField(primary_key=True)
    category=models.ForeignKey(categorylist, on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    title=models.CharField(max_length=100)
    video=EmbedVideoField()


    desc=models.TextField()
    publish=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-title',)

    def __str__(self):
        return self.title
        


class VideoComment(models.Model):
    srno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article= models.ForeignKey(Item, on_delete=models.CASCADE)    
    parent= models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp= models.DateTimeField(default = now)
    def __str__(self):
        return self.comment[0:10] + "..." + self.user.username