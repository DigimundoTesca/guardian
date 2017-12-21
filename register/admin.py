from django.contrib import admin
from .models import *


@admin.register(Delivery)
class AdminDelivery(admin.ModelAdmin):
    list_display = ('id', 'trailer', 'number', 'date', 'units', 'product', 'total', 'deliver',)
