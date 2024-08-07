# Generated by Django 5.0.6 on 2024-07-06 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistify', '0008_remove_requestforquote_shipment_destination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforquote',
            name='shipment_destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rfq_destination_shipments', to='logistify.port'),
        ),
        migrations.AlterField(
            model_name='requestforquote',
            name='shipment_origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rfq_origin_shipments', to='logistify.port'),
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='shipment_destination',
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipment_origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_shipments', to='logistify.port'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='shipment_destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_shipments', to='logistify.port'),
        ),
    ]
