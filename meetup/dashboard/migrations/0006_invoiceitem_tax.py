# Generated by Django 3.0.6 on 2020-05-19 20:41

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200519_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.2'), max_digits=10),
        ),
    ]
