# Generated by Django 3.2.4 on 2021-06-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pay_Mob', '0009_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='Pay_Mob.Products'),
        ),
    ]