from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=256)

class Equipment(models.Model):
	name = models.CharField(max_length=250)
	mrl = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], default=0)

