from django.db import models
import django_tables2 as tables
from django.core.validators import MinValueValidator, MaxValueValidator

class Equipment(models.Model):
	name = models.CharField(max_length=250)
	def __str__(self):
		return self.name
	mrl = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(3)], default=0)

class Part(models.Model):
	name = models.ForeignKey(Equipment, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
	#  remove later on otherwise both will be deleted