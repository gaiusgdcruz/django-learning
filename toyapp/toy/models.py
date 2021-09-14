from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Company(models.Model):
    comp_name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    email_id = models.EmailField()

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.comp_name

class Toy(models.Model):
    toy_name = models.CharField(max_length=30)
    company = models.ForeignKey(Company,on_delete=CASCADE)
    cost = models.IntegerField()

    def __str__(self):
        return self.toy_name
    
