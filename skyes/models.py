from datetime import timezone
from django.db import models

from IpekProject import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):

        self.save()

    def __str__(self):
        return self.title
# Create your models here.
