# Generated by Django 4.1.2 on 2022-11-21 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_orderitems_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='total_price',
            field=models.CharField(blank=True, default='111111', max_length=300, null=True, verbose_name='total_price'),
        ),
    ]
