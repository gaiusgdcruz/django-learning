from django.db import models

# Create your models here.

class Transformer(models.model):
    name = models.CharField(max_length=150,unique=True)
    alternate_mode = models.CharField(max_length=250,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    alive = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-id')

    def __str__(self):
        return self.name