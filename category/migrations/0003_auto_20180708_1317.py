# Generated by Django 2.0.7 on 2018-07-08 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20180704_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
    ]