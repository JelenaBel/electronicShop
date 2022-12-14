# Generated by Django 4.1.2 on 2022-10-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_product_main_description_product_anons_eng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='ask', max_length=100, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='anons_eng',
            field=models.CharField(max_length=300, verbose_name='anons_eng'),
        ),
        migrations.AlterField(
            model_name='product',
            name='anons_fi',
            field=models.CharField(max_length=300, verbose_name='anons_fi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='guaranty',
            field=models.BooleanField(default='True', verbose_name='guaranty'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.CharField(max_length=400, verbose_name='image1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.CharField(max_length=400, verbose_name='image2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.CharField(max_length=400, verbose_name='image3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_description_eng',
            field=models.TextField(verbose_name='Main_description_eng'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_description_fi',
            field=models.TextField(verbose_name='Main_description_fi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='service_center',
            field=models.BooleanField(default='True', verbose_name='service_center'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=100, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(max_length=100, verbose_name='weight'),
        ),
    ]
