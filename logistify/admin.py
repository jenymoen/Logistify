from django.contrib import admin
from .models import Shipment, Port,RequestForQuote

admin.site.register(Shipment)
admin.site.register(Port)
admin.site.register(RequestForQuote)

# Register your models here.
