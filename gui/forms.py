from django import forms
from django_popup_view_field.fields import PopupViewField
from .popups import ColorsPopupView

class ColorForm(forms.Form):

    color = PopupViewField(
        view_class=ColorsPopupView,
        popup_dialog_title='What is your favorite color',
        required=True,
        help_text='be honest'
    )
