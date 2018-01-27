from string import ascii_uppercase
from django.shortcuts import render

from django import forms
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from .models import Equipment
from .tables import EquipmentTable
from django_tables2 import RequestConfig

from django_popup_view_field.registry import registry_popup_view

from .models import Country


class SexPopupView(TemplateView):
    template_name = "popups/popup_sex.html"


class ColorPopupView(TemplateView):
    template_name = "popups/popup_color.html"


class CountryPopupView(TemplateView):

    template_name = "popups/popup_country.html"
    countries = None

    def get(self, request, *args, **kwargs):
        qs = Country.objects.none()
        if "code" in request.GET or "name" in request.GET:
            qs = Country.objects.all()
            if "code" in request.GET:
                qs = qs.filter(code__istartswith=request.GET.get('code'))
            if "name" in request.GET:
                qs = qs.filter(name__icontains=request.GET.get('name'))

        self.countries = qs
        return super(CountryPopupView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CountryPopupView, self).get_context_data(**kwargs)
        context['countries'] = self.countries
        context['ascii_uppercase'] = ascii_uppercase
        return context


class TablePopupView(TemplateView):
    template_name = "popups/table.html"

    def get(self, request, *args, **kwargs):
        table = EquipmentTable(Equipment.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'popups/table.html', {'table': table})


# Register popup views
registry_popup_view.register(SexPopupView)
registry_popup_view.register(ColorPopupView)
registry_popup_view.register(CountryPopupView)
registry_popup_view.register(TablePopupView)