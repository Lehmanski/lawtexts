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
from .forms import DemoForm


class EquipmentView(TemplateView):
    template_name = "gui/index.html"

    def get(self, request, *args, **kwargs):
        table = EquipmentTable(Equipment.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'gui/index.html', {'table': table})


class DeleteView(TemplateView):
    template_name = "gui/test.html"

    def get(self, request, *args, **kwargs):
        table = EquipmentTable(Equipment.objects.all())
        del_id = int(kwargs['user_id'])
        Equipment.objects.filter(id=del_id).delete()
        RequestConfig(request).configure(table)
        return render(request, 'gui/test.html', {'table': table})


class Index(TemplateView):
    template_name = "demo/index.html"
    form_class = DemoForm

    form_1 = None
    form_2 = None
    form_3 = None

    def get(self, request, *args, **kwargs):
        self.form_1 = self.form_class(request, prefix="form_1")
        self.form_2 = self.form_class(request, prefix="form_2")
        self.form_3 = self.form_class(request, prefix="form_3")
        # return super(Index, self).get(request, *args, **kwargs)
        table = EquipmentTable(Equipment.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'demo/index.html', {'table': table})

    def post(self, request, *args, **kwargs):
        self.form_1 = self.form_class(prefix="form_1", data=request.POST)
        self.form_2 = self.form_class(prefix="form_2", data=request.POST)
        self.form_3 = self.form_class(prefix="form_3", data=request.POST)

        self.form_1.is_valid()
        self.form_2.is_valid()
        self.form_3.is_valid()

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["form_1"] = self.form_1
        context["form_2"] = self.form_2
        context["form_3"] = self.form_3
        return context
        
