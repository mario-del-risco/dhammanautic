from django.db import models


# Create your models here.

class Resource(models.Model):
    title = models.CharField(max_length=100)
    main_goal = models.TextField()
    slug = models.SlugField(blank=True)
    summary = models.TextField(blank=True)
    thumb = models.ImageField(default='default.png', blank=True)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

