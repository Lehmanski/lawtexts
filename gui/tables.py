import django_tables2 as tables
from .models import Equipment
from django.utils.html import escape
from django.utils.safestring import mark_safe
from .popups import ColorsPopupView

class MyColumns(tables.Column): 
	empty_values = list() 
	def render(self, value, record): 
		return mark_safe('<button id="%s" class="btn btn-info">edit</button>' % escape('<a href="% url" ColorsPopupView>'))

class EquipmentTable(tables.Table):
	edit = MyColumns()
	class Meta:
		model = Equipment
		template = 'django_tables2/bootstrap.html'