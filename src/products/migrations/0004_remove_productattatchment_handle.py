# Generated by Django 4.1.13 on 2024-01-28 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productattatchment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattatchment',
            name='handle',
        ),
    ]
