# Generated by Django 4.1.2 on 2022-11-06 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_productcategory_parent_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='parent_category',
            field=models.CharField(max_length=100, verbose_name=models.CharField(max_length=100, verbose_name='Category name')),
        ),
    ]
