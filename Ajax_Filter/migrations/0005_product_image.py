# Generated by Django 3.2.4 on 2021-06-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ajax_Filter', '0004_filter_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='asd', upload_to=''),
            preserve_default=False,
        ),
    ]
