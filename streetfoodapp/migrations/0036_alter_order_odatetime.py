# Generated by Django 5.0.6 on 2024-06-19 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetfoodapp', '0035_alter_order_odatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='odatetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 19, 18, 2, 27, 51191)),
        ),
    ]
