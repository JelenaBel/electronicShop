# Generated by Django 4.1.2 on 2022-10-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='mobile', max_length=16, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='guaranty',
            field=models.CharField(max_length=400, verbose_name='guaranty'),
        ),
        migrations.AlterField(
            model_name='product',
            name='service_center',
            field=models.CharField(max_length=400, verbose_name='service_center'),
        ),
    ]
