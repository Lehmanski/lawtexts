from django.conf.urls import include, url
from .views import EquipmentView, DeleteView, Index

urlpatterns = [
    #url(r'^$', EquipmentView.as_view(), name="index"),
    url(r'^del/(?P<user_id>\d+)/$', DeleteView.as_view(), name='delete'),
    url(r'^$', Index.as_view(), name="index"),
    # django-popup-view-field
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls')),
]