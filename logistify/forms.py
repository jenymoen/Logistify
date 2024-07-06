from django import forms
from django.db import models
from .models import Shipment, RequestForQuote
from django.forms import ModelForm
from django.forms.widgets import DateInput

# For the user creation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class DateInput(forms.DateInput):
    input_type = "date"

class DateForm(forms.Form):
    date = forms.DateField(widget=DateInput)


class ShipmentForm(ModelForm):
    class Meta:
        model = Shipment
        fields = [
            "shipment_name",
            "shipment_description",
            "cargo_ready_date",
            "shipment_weight",
            "shipment_volume",
            "shipment_value",
            "shipment_destination",
            "shipment_origin",
        ]


class RFQForm(ModelForm):
    class Meta:
        model = RequestForQuote
        fields = [
            "shipment_name",
            "shipment_description",
            "cargo_ready_date",
            "shipment_weight",
            "shipment_volume",
            "shipment_value",
            "shipment_destination",
            "shipment_origin",
        ]
        widgets = {"cargo_ready_date": DateInput()}