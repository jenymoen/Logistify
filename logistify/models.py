from django.db import models
from django.db.models.enums import Choices


class shipment(models.Model):
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
  shipment_origin = models.CharField(max_length=100, null=True, blank=True)
  expected_delivery_date = models.DateField(null=True, blank=True)

  objects = models.Manager()

  def __str__(self):
    return self.shipment_name+" - "+self.shipment_description

class supplier(models.Model):
  supplier_name = models.CharField(max_length=100, null=True, blank=True)
  
