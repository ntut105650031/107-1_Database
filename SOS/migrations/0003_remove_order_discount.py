# Generated by Django 2.1.3 on 2018-12-22 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SOS', '0002_auto_20181222_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
    ]