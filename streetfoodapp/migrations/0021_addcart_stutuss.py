# Generated by Django 3.2.9 on 2022-04-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetfoodapp', '0020_remove_addcart_stutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcart',
            name='stutuss',
            field=models.IntegerField(default=0),
        ),
    ]
