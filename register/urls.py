from django.conf.urls import url
from . import views
from .views import ReportDelivery

app_name = 'register'

urlpatterns = [
    url(r'^$', views.index, name='inicio'),
    url(r'^correo/$', views.mail, name='correo'),
    url(r'^reporte/$', ReportDelivery.as_view(), name='report'),
]
