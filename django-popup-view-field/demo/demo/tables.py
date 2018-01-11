import django_tables2 as tables
from .models import Equipment

class EquipmentTable(tables.Table):
	class Meta:
		model = Equipment