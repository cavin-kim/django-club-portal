from django.db import models


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
