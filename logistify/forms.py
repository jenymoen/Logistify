from django import forms
from django.db import models
from .models import Shipment, RequestForQuote
from django.forms import ModelForm



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