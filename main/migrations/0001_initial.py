# Generated by Django 4.1.2 on 2022-10-13 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(verbose_name='ID')),
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Name')),
                ('main_description', models.TextField(verbose_name='Main_description')),
            ],
        ),
    ]
