from django.shortcuts import render, redirect
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
    
def createRFQ(request):

    form = RFQForm()
    if request.method == "POST":
        form = RFQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/shipment/")

    context = {"form": form}

    return render(request, "create_RFQ.html", context)
    
    
    
    
    # form = ShipmentForm(instance=shipment)




  