# Generated by Django 2.1.3 on 2018-12-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profits', models.PositiveIntegerField(verbose_name='訂單利潤')),
            ],
        ),
    ]
