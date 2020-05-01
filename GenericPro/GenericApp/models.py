from django.db import models

# Create your models here.


class Emp(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=200)
    esal = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
