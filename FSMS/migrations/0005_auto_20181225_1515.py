# Generated by Django 2.1.3 on 2018-12-25 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SOS', '0008_auto_20181225_1515'),
        ('MCS', '0005_merge_20181225_0933'),
        ('FSMS', '0004_remove_checkorder_sold_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkorder',
            old_name='empolyee_id',
            new_name='employee_id',
        ),
        migrations.AlterUniqueTogether(
            name='checkorder',
            unique_together={('order_no', 'employee_id')},
        ),
    ]
