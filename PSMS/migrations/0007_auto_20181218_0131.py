# Generated by Django 2.1.3 on 2018-12-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSMS', '0006_auto_20181218_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='kind_chose',
            field=models.CharField(choices=[('Beef', '牛肉'), ('Chicken', '雞肉'), ('Mix', '混合'), ('Pork', '豬肉'), ('Seafood', '海鮮'), ('Vegetable', '蔬菜')], max_length=10, null=True, verbose_name='種類'),
        ),
    ]