# Generated by Django 2.0.7 on 2018-07-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_is_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
