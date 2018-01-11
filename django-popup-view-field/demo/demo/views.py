from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Equipment
from .tables import EquipmentTable
from .forms import DemoForm


class Index(TemplateView):
    template_name = "demo/index.html"
    form_class = DemoForm

    form_1 = None
    def get(self, request, *args, **kwargs):
        self.form_1 = self.form_class(prefix="form_1")
        return super(Index, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form_1 = self.form_class(prefix="form_1", data=request.POST)

        self.form_1.is_valid()

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["form_1"] = self.form_1
        return context

class EquipmentView(TemplateView):
    template_name="demo/table.html"
    def get(self, request, *args, **kwargs):
        data = Equipment.objects.all()
        context = self.get_context_data(**kwargs)
        context['table'] = data
        return self.render_to_response(context)
    Index.as_view()