from django.shortcuts import render, redirect, get_object_or_404
from .models import Shipment, Port, RequestForQuote, Item, CommodityClassification
from .forms import *
from django.utils.timezone import datetime
import requests, json


#views code for login function
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)
    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)
    
def logoutUser(request):
    logout(request)
    return redirect('login')



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

def shipment_detail_view(request, pk):
    shipment_detailview = get_object_or_404(Shipment, id=pk)
    shipment = Shipment.objects.all()

    context = {
        "shipment_detailview": shipment_detailview,
        "shipment": shipment,
        
    }

    return render(request, "shipment_details.html", context)
    
def createRFQ(request):

    form = RFQForm()
    if request.method == "POST":
        form = RFQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/shipment_list/")

    context = {"form": form}

    return render(request, "create_RFQ.html", context)
    
   
def rfq_list(request):
    rfq = RequestForQuote.objects.all()
    port = Port.objects.all()

    context = {
            "rfq": rfq,
            "port": port,

        }  
    return render(request, "rfq_list.html", context)   
    
    # form = ShipmentForm(instance=shipment)


def item_list(request):
    item = Item.objects.all()

    context = {
            "item": item,
    }
    return render(request, "item_list.html", context)



def populate_commodity_classifications():
    response = requests.get('https://api.maersk.com/commodity-classifications?commodityName=all&cargoType=DRY')
    if response.status_code == 200:
        commodities = response.json()  # Assuming the response is a JSON list
        for commodity in commodities:
            CommodityClassification.objects.create(
                commodity_id=commodity['commodityCode'],
            )

  