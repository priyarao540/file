# Generated by Django 3.0.8 on 2020-09-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gauranj', '0019_temp2_is_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('is_delete', models.BooleanField(null=True)),
            ],
        ),
    ]