from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    post_sno=models.AutoField(primary_key=True)
    post_title=models.CharField(max_length=200)
    post_desc=models.CharField(max_length=10000)
    post_author=models.CharField(max_length=40)
    post_views=models.IntegerField(default=0)
    post_slug=models.CharField(max_length=90,default='')
    post_ts=models.DateTimeField(blank=True)

    def __str__(self):
        return self.post_title

class blogcomment(models.Model):
    comm_sno=models.AutoField(primary_key=True)
    comm_comment=models.TextField()
    comm_slug=models.CharField(max_length=90,default='')
    comm_user=models.ForeignKey(User,on_delete=models.CASCADE)
    comm_post=models.ForeignKey(post,on_delete=models.CASCADE)
    comm_parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    comm_ts=models.DateTimeField(default=now)

    def __str__(self):
        return self.comm_comment