from django.conf.urls import include, url
from .views import EquipmentView, DeleteView

urlpatterns = [
    url(r'^$', EquipmentView.as_view(), name="index"),
    url(r'^del/(?P<user_id>\d+)/$', DeleteView.as_view(), name='delete'),
    # django-popup-view-field
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls'))
]