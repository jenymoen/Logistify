from django.shortcuts import render, redirect
from .models import Shipment, Port, RequestForQuote
from .forms import *
from django.utils.timezone import datetime


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




  