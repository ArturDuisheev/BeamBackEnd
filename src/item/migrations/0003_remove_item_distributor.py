# Generated by Django 5.0.3 on 2024-03-28 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_distributor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='distributor',
        ),
    ]