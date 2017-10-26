from django.db import models

# Create your models here.
class employees(models.Model):
    firstanme = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    #Method that returns all the fields declared above (string representation)
    def __str__(self):
        return self.firstanme
