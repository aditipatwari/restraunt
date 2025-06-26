from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.FloatField()

class our_user(models.Model):
    email = models.EmailField(null=True)
    password = models.IntegerField(null=True)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "CustomUser"


