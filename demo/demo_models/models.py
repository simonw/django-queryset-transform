from django.db import models
from queryset_transform import TransformManager

class Tag(models.Model):
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length = 255)
    tags = models.ManyToManyField(Tag)
    
    objects = TransformManager()
    
    def __unicode__(self):
        return self.name
