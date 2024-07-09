from django import forms
from django.db import models
from .models import Shipment, RequestForQuote
from django.forms import ModelForm
from django.forms.widgets import DateInput


# for the Django Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, HTML, Button, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

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

    def __init__(self, *args, **kwargs):
        super(ShipmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("shipment_name", css_class="my-class"),
            'shipment_description',
        )
        self.helper.add_input(Submit("submit", "Submit"))


class RFQForm(ModelForm):
    shipment_volume = forms.FloatField(required=False, label='Shipment Volume', widget=forms.HiddenInput())
    shipment_length = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_shipment_length'}))
    shipment_width = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_shipment_width'}))
    shipment_height = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_shipment_height'}))


    class Meta:
        model = RequestForQuote
        fields = [
            "shipment_name",
            "shipment_description",
            "cargo_ready_date",
            "shipment_weight",
            "shipment_length",
            "shipment_width",
            "shipment_height",
            "shipment_value",
            "shipment_destination",
            "shipment_origin",
        ]
        widgets = {"cargo_ready_date": DateInput()}

    def __init__(self, *args, **kwargs):
            super(RFQForm, self).__init__(*args, **kwargs)
            # Calculate shipment_volume if length, width, and height are available
            length = self.initial.get('shipment_length', 0)
            width = self.initial.get('shipment_width', 0)
            height = self.initial.get('shipment_height', 0)
            volume = length * width * height
            self.fields['shipment_volume'].initial = volume
            self.fields['shipment_volume'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        shipment_volume = cleaned_data.get('shipment_volume')

        if shipment_volume <= 0:
            self.add_error('shipment_volume', 'Shipment volume must be greater than 0')

        return cleaned_data