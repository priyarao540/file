# Generated by Django 3.0.8 on 2020-08-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gauranj', '0005_comblog_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comblog',
            name='password',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='comblog',
            name='reenterpassword',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
