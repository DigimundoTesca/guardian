from django.conf.urls import url
from . import views

app_name = 'register'

urlpatterns = [
    url(r'^$', views.index, name='inicio'),
    url(r'^correo/$', views.mail, name='correo'),
]
