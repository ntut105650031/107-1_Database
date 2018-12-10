# Generated by Django 2.1.3 on 2018-12-10 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MCS', '0002_auto_20181210_1315'),
        ('SOS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profits', models.PositiveIntegerField(verbose_name='訂單利潤')),
                ('empolyee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCS.Employee', verbose_name='員工帳號')),
                ('order_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SOS.Order', verbose_name='訂單編號')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='checkorder',
            unique_together={('order_no', 'empolyee_id')},
        ),
    ]
