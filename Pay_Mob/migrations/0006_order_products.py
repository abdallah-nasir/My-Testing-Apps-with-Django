# Generated by Django 3.2.4 on 2021-06-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pay_Mob', '0005_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(null=True, to='Pay_Mob.Products'),
        ),
    ]