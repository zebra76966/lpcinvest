# Generated by Django 3.1.7 on 2022-12-01 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20221201_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='city',
            field=models.CharField(choices=[('1', 'birmingham'), ('2', '\tbolton'), ('3', 'leeds')], max_length=20),
        ),
        migrations.AlterField(
            model_name='properties',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 1, 20, 10, 35, 463925)),
        ),
    ]
