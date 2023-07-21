from django.db import models

class ShortUrl(models.Model):
    short_url = models.CharField(max_length=15 , unique=True)
    long_url = models.URLField(max_length=200)

    def __str__(self):
        return self.short_url
    
