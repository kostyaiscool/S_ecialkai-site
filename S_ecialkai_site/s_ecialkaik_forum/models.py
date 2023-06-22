from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=90, null=False)
    text = models.TextField()
    file = models.FileField(blank=True, null = True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)