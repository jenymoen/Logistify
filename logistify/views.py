from django.shortcuts import render
from .models import Shipment


def index(request):
    return render(request, 'index.html', {})

def shipment_list(request):
    shipments = Shipment.object.all()
    context = {

    }

    return render(request, "shipment_list.html", context)

  