from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    post_count = models.IntegerField(blank=True, null=True, default=0)
class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    text = models.TextField()
    file = models.FileField(blank=True, null = True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)