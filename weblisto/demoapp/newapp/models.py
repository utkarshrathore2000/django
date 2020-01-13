from django.db import models

# Create your models here.
# Create your models here.
class Employee(models.Model):
    employe_id=models.IntegerField()
    employe_name=models.CharField(max_length=100)
    employe_email=models.EmailField()
    employe_contact=models.CharField(max_length=15)
    employe_address=models.CharField(max_length=20)

