from django.db import models
from django_lazymap import LazyMapManager

class Tag(models.Model):
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length = 255)
    tags = models.ManyToManyField(Tag)
    
    objects = LazyMapManager()
    
    def __unicode__(self):
        return self.name
