# Generated by Django 3.2.4 on 2021-06-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pay_Mob', '0006_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
    ]
