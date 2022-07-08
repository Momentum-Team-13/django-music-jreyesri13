from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    artist = models.CharField(max_length=255, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
