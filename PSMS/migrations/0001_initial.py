# Generated by Django 2.1.3 on 2018-12-12 07:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('pizza_no', models.AutoField(primary_key=True, serialize=False, verbose_name='披薩編號')),
                ('name', models.CharField(max_length=20, verbose_name='披薩名稱')),
                ('description', models.TextField(verbose_name='披薩描述')),
                ('price', models.PositiveIntegerField(verbose_name='披薩價格')),
                ('size', models.CharField(max_length=2, verbose_name='披薩尺寸')),
                ('cost', models.PositiveIntegerField(verbose_name='披薩成本')),
                ('in_stock', models.PositiveIntegerField(verbose_name='披薩庫存量')),
                ('sales_volume', models.PositiveIntegerField(default=0, verbose_name='披薩銷售量')),
                ('click_count', models.PositiveIntegerField(default=0, verbose_name='披薩點擊量')),
                ('isVegetarian', models.BooleanField(verbose_name='是否為素食披薩')),
                ('stars', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(1, '最低1分'), django.core.validators.MaxValueValidator(5, '最多5分')], verbose_name='披薩評分')),
            ],
        ),
    ]
