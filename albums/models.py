from django.db import models

# Create your models here.

class Album(models.Model):
    

    title = models.CharField(max_length=255,null=True, blank=True)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, null=True, blank=True, related_name="albums")
    year_released = models.DateField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class Artist(models.Model):

    name = models.CharField(max_length=255,null=True, blank=True)
    hometown = models.CharField(max_length=255,null=True, blank=True)
    biography = models.TextField(max_length=255,null=True, blank=True)
