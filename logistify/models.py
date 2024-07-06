from django.db import models
from django.db.models.enums import Choices



class Port(models.Model):
  port_code = models.CharField(max_length=5, null=True, blank=True)
  port_name = models.CharField(max_length=30, null=True, blank=True)
  port_city = models.CharField(max_length=100, null=True, blank=True)
  port_type = models.CharField(max_length=100, null=True, blank=True)
  latitude = models.FloatField(null=True, blank=True)
  longitude = models.FloatField(null=True, blank=True)

  def __str__(self):
    return f"{self.port_code+" - "+self.port_name}"


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
  shipment_origin = models.CharField(max_length=50, null=True, blank=True)
  shipment_destination = models.ManyToManyField(Port)
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
  shipment_volume = models.FloatField(null=True, blank=True)
  shipment_value = models.FloatField(null=True, blank=True)
  shipment_cost = models.FloatField(null=True, blank=True)
  shipment_origin = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='origin_shipments')
  shipment_destination = models.ForeignKey(Port, on_delete=models.CASCADE, related_name='destination_shipments')
  expected_delivery_date = models.DateField(null=True, blank=True)
  

  objects = models.Manager()

  def __str__(self):
    return self.shipment_name+" - "+self.shipment_description




class Supplier(models.Model):
  supplier_name = models.CharField(max_length=100, null=True, blank=True)
  

