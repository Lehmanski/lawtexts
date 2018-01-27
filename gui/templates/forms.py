from crispy_forms.helper import FormHelper
from django import forms
from .models import Equipment
from .tables import EquipmentTable
from django_tables2 import RequestConfig

from django_popup_view_field.fields import PopupViewField

from .popups import ColorPopupView, CountryPopupView, SexPopupView


class DemoForm(forms.Form):

    name = forms.CharField(label="Name")

    sex = PopupViewField(
        # Attrs for popup
        view_class=SexPopupView,
        popup_dialog_title='What is your SEX',
        # Attr for CharField
        required=True,
        help_text='female or male'
    )

    color = PopupViewField(view_class=ColorPopupView)
    country_code = PopupViewField(view_class=CountryPopupView)

    def __init__(self, request, *args, **kwargs):
        super(DemoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
