# Generated by Django 5.0.6 on 2024-06-28 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='expected_delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]