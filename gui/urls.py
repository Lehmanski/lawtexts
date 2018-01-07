from django.conf.urls import include, url
from .views import EquipmentView

urlpatterns = [
    url(r'^$', EquipmentView.as_view(), name="index"),
    # django-popup-view-field
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls'))
]