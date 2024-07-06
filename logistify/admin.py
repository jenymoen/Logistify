from django.contrib import admin
from .models import Shipment, Port, Quote

admin.site.register(Shipment)
admin.site.register(Port)
admin.site.register(Quote)
# Register your models here.