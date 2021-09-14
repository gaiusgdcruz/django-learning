from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email_id = models.EmailField()

    def __str__(self):
        return self.company_name

class Toys(models.Model):
    toy_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,blank=True,null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.toy_name

