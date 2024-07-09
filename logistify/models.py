from typing import Iterable
from django.db import models
from django.db.models.enums import Choices


class UnitOfMeasure(models.Model):
    uom_id = models.CharField(max_length=5, null=True, blank=True)
    uom_description = models.CharField(max_length=50)


    
class Port(models.Model):
  port_code = models.CharField(max_length=5, null=True, blank=True)
  port_name = models.CharField(max_length=30, null=True, blank=True)
  port_city = models.CharField(max_length=100, null=True, blank=True)
  port_type = models.CharField(max_length=100, null=True, blank=True)
  latitude = models.FloatField(null=True, blank=True)
  longitude = models.FloatField(null=True, blank=True)

  def __str__(self):
    return f"{self.port_code+" - "+self.port_name}"

class Contact(models.Model):
  contact_name = models.CharField(max_length=100, null=True, blank=True)
  contact_email = models.EmailField(max_length=100, null=True, blank=True)
  contact_phone = models.CharField(max_length=100, null=True, blank=True)
  contact_address = models.CharField(max_length=100, null=True, blank=True)
  contact_city = models.CharField(max_length=100, null=True, blank=True)
  contact_state = models.CharField(max_length=100, null=True, blank=True)
  contact_country = models.CharField(max_length=100, null=True, blank=True)
  contact_zip = models.CharField(max_length=100, null=True, blank=True)
  contact_type = models.CharField(max_length=100, null=True, blank=True)
  contact_company = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return self.contact_name+" - "+self.contact_email

class Contact(models.Model):
  contact_name = models.CharField(max_length=100, null=True, blank=True)
  contact_email = models.EmailField(max_length=100, null=True, blank=True)
  contact_phone = models.CharField(max_length=100, null=True, blank=True)
  contact_address = models.CharField(max_length=100, null=True, blank=True)
  contact_city = models.CharField(max_length=100, null=True, blank=True)
  contact_state = models.CharField(max_length=100, null=True, blank=True)
  contact_country = models.CharField(max_length=100, null=True, blank=True)
  contact_zip = models.CharField(max_length=100, null=True, blank=True)
  contact_type = models.CharField(max_length=100, null=True, blank=True)
  contact_company = models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return self.contact_name+" - "+self.contact_email

class Supplier(models.Model):
  supplier_name = models.CharField(max_length=100, null=True, blank=True)
  supplier_contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='supplier_contacts', null=True, blank=True)
  supplier_address = models.CharField(max_length=100, null=True, blank=True)
  loading_bay = models.BooleanField(default=False)

class Shipment(models.Model):
  shipment_name = models.CharField(max_length=100, null=True, blank=True)
  shipment_description = models.CharField(max_length=100, null=True, blank=True)
  shipment_status = models.CharField(max_length=100, null=True, blank=True)
  cargo_ready_date = models.DateField(null=True, blank=True)
  shipment_date = models.DateField(null=True, blank=True)
  shipment_time = models.TimeField(null=True, blank=True)
  shipment_weight = models.FloatField(null=True, blank=True)
  shipment_volume = models.FloatField(null=True, blank=True)
  shipment_value = models.FloatField(null=True, blank=True)
  shipment_cost = models.FloatField(null=True, blank=True)
  shipment_origin = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='origin_shipments', null=True, blank=True)
  shipment_destination = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='destination_shipments', null=True, blank=True)
  expected_delivery_date = models.DateField(null=True, blank=True)
  

  objects = models.Manager()

  def __str__(self):
    return self.shipment_name+" - "+self.shipment_description

class RequestForQuote(models.Model):
    shipment_name = models.CharField(max_length=100, null=True, blank=True)
    shipment_description = models.CharField(max_length=100, null=True, blank=True)
    shipment_status = models.CharField(max_length=100, null=True, blank=True)
    cargo_ready_date = models.DateField(null=True, blank=True)
    shipment_date = models.DateField(null=True, blank=True)
    shipment_time = models.TimeField(null=True, blank=True)
    shipment_weight = models.FloatField(null=True, blank=True)
    shipment_length = models.FloatField(null=True, blank=True)
    shipment_width = models.FloatField(null=True, blank=True)
    shipment_height = models.FloatField(null=True, blank=True)
    shipment_volume = models.FloatField(editable=False, null=True, blank=True)
    shipment_value = models.FloatField(null=True, blank=True)
    shipment_cost = models.FloatField(null=True, blank=True)
    shipment_origin = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='rfq_origin_shipments', null=True, blank=True)
    shipment_destination = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='rfq_destination_shipments', null=True, blank=True)
    expected_delivery_date = models.DateField(null=True, blank=True)
  
    def save(self, *args, **kwargs):
      self.shipment_volume = self.shipment_length * self.shipment_width * self.shipment_height
      super(RequestForQuote, self).save(*args, **kwargs)

    def __str__(self):
      return self.shipment_name+" - "+self.shipment_description

class Item(models.Model):
    item_number = models.IntegerField(null=True,blank=True)
    item_name = models.CharField(max_length=100, null=True, blank=True)
    item_value = models.FloatField(null=True, blank=True)
    item_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, related_name="items", null=True, blank=True)
    item_HSS_code = models.CharField(max_length=15, null=True, blank=True)
    item_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True, related_query_name="suppliername")
    item_supplier_item_number = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
      return self.item_number+" - "+self.item_name
    


class CommodityClassification(models.Model):
    commodity_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name