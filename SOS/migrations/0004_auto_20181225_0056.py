# Generated by Django 2.1.3 on 2018-12-24 16:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SOS', '0003_remove_order_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False, verbose_name='折扣代碼')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='折扣名稱')),
                ('description', models.TextField(default='', verbose_name='折扣描述')),
                ('rate', models.DecimalField(decimal_places=2, default=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0, '0<=折扣<=1'), django.core.validators.MaxValueValidator(1, '0<=折扣<=1')], verbose_name='折扣率')),
                ('kind', models.CharField(choices=[('shipping', '運費'), ('seasoning', '季節性折扣'), ('special', '特殊折扣')], default='shipping', max_length=10, verbose_name='種類')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='isFreeShipping',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='DiscountFare',
            fields=[
                ('discount_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='SOS.Discount', verbose_name='折扣代碼')),
                ('sill', models.PositiveIntegerField(verbose_name='目標金額')),
            ],
        ),
        migrations.CreateModel(
            name='DisountOrder',
            fields=[
                ('discount_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='SOS.Discount', verbose_name='折扣代碼')),
                ('startDate', models.DateTimeField(verbose_name='優惠開始日期')),
                ('endDate', models.DateTimeField(verbose_name='優惠截止日期')),
            ],
        ),
        migrations.AddField(
            model_name='discountitem',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theDiscount', to='SOS.Discount'),
        ),
        migrations.AddField(
            model_name='discountitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theOrder', to='SOS.Order'),
        ),
    ]