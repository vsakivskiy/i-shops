# Generated by Django 2.0.7 on 2018-07-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productgeneric'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
    ]
