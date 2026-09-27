from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    class Meta:
        verbose_name = "Stream Platform"
        verbose_name_plural = "Stream Platforms"

    def __str__(self):
        return self.name
