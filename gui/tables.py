import django_tables2 as tables
from .models import Equipment
from django.utils.html import escape
from django.utils.safestring import mark_safe
from .popups import ColorsPopupView

class Edit(tables.Column): 
	empty_values = list() 
	def render(self, value, record): 
		button_edit = str('<button id="edit-%s" class="btn-edit">Edit</button>' % escape(record.id))
		return mark_safe(button_edit)
		
class Remove(tables.Column):
	empty_values = list()
	def render(self, value, record):
		button_remove = str('<button id="%s" class="btn-remove">Remove</button>' % escape(record.id))
		return mark_safe(button_remove)

class EquipmentTable(tables.Table):
	edit = Edit()
	remove = Remove()
	class Meta:
		model = Equipment
		template = 'django_tables2/bootstrap.html'