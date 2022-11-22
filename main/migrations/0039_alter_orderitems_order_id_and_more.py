# Generated by Django 4.1.2 on 2022-11-21 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_orderitems_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='order_id',
            field=models.ForeignKey(max_length=300, on_delete=django.db.models.deletion.PROTECT, to='main.orders'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='total_price',
            field=models.CharField(max_length=300, verbose_name='total_price'),
        ),
    ]