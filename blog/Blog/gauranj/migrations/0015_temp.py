# Generated by Django 3.0.8 on 2020-09-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gauranj', '0014_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(null=True)),
            ],
        ),
    ]
