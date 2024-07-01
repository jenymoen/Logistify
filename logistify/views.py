from django.shortcuts import render
from .models import Shipment, Port
from .forms import *


def index(request):
    return render(request, 'index.html', {})

def shipment_list(request):
    shipment = Shipment.objects.all()
    port = Port.objects.all()

    context = {
        "shipment": shipment,
        "port": port,

    }  
    return render(request, "shipment_list.html", context)

def shipment_detailView(request, pk):
    shipment_detailview = Shipment.objects.get(id=pk)
    shipment = Shipment.objects.all()

    context = {
        
    }

    return render(request, "shipment_details.html", context)
    
    
    
    
    
    
    # form = ShipmentForm(instance=shipment)




  