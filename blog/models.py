from django.db import models
from datetime import date, datetime


# this class is for blog details
class Post(models.Model):
    name = models.TextField(blank=True)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    politics = models.CharField(max_length=50)
    lifestyle = models.CharField(max_length=100)
    markviews = models.IntegerField()
    post_date = models.DateField(default=date.today)
    views = models.DecimalField(max_digits=4, decimal_places=1)
    post_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    parent_id = models.IntegerField(blank=True)
    post_id = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    timedate = models.DateTimeField(datetime.now, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    comment = models.TextField()

    def __str__(self):
        return self.name
