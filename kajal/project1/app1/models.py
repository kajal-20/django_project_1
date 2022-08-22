from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    email = models.EmailField()
    image = models.ImageField(upload_to='img',blank=True,null=True)

    def get_absolute_url(self):
        return reverse("single_url",kwargs={'pk':self.pk})