# Generated by Django 3.2.4 on 2021-06-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pay_Mob', '0003_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=True),
        ),
    ]
