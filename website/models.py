from django.db import models


# Create your models here.
class MyModel(models.Model):

    Id = models.BigAutoField(primary_key=True)
    Name = models.CharField("Name", max_length=50)
    Date = models.DateField()
    IsActive = models.BooleanField(default=True)
    Description = models.IntegerField()

    def ___str___(self):
        return self.Name  # Replace with an appropriate field for the string representation
