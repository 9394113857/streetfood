# Generated by Django 5.0.6 on 2024-06-24 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetfoodapp', '0040_alter_order_odatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='odatetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 24, 18, 52, 50, 161051)),
        ),
    ]
