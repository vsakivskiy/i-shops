# Generated by Django 2.0.7 on 2018-07-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('named_id', models.CharField(max_length=30, unique=True)),
                ('is_active', models.BooleanField()),
                ('is_brand', models.BooleanField()),
                ('container_type', models.CharField(max_length=10)),
                ('per_item', models.DecimalField(decimal_places=4, max_digits=8)),
            ],
        ),
    ]
