# Generated by Django 3.2.9 on 2022-04-09 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streetfoodapp', '0013_remove_addcart_merchant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcart',
            name='food',
        ),
    ]
