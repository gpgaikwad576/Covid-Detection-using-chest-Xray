# Generated by Django 3.2 on 2021-06-03 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_alter_mcount_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='gender',
            field=models.CharField(choices=[('1', 'doctor'), ('2', 'nurse'), ('3', 'radiologist'), ('4', 'Pharmacy'), ('5', 'other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='mcount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 3, 15, 47, 27, 713673), null=True),
        ),
    ]
