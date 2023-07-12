from django.db import models

# Create your models here.
class MyModel(models.Model):

    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField()
    # TODO add fields

    def ___str_(self):
        return self.field1  # Replace with an appropriate field for the string representation
