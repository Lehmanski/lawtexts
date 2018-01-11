'''
from django.http import HttpResponse
from django.template import loader
from .models import Equipment


def index(request):
    all_equip = Equipment.objects.all()
    template = loader.get_template('gui/index.html')
    context = {
    	'all_equip': all_equip,
    }
    return HttpResponse(template.render(context, request))
'''
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Equipment
from .tables import EquipmentTable
from django.views.generic import TemplateView
from django.http import HttpResponse

class EquipmentView(TemplateView):
    template_name="gui/index.html"
    def get(self, request, *args, **kwargs):
        table = EquipmentTable(Equipment.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'gui/index.html', {'table': table})
class DeleteView(TemplateView):
    template_name="gui/test.html"
    def get(self, request,*args, **kwargs):
        table = EquipmentTable(Equipment.objects.all())
        del_id = int(kwargs['user_id'])
        Equipment.objects.filter(id=del_id).delete()
        RequestConfig(request).configure(table)
        return render(request, 'gui/test.html', {'table': table})