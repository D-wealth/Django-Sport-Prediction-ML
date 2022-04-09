# Generated by Django 3.2.6 on 2022-04-08 07:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('height', models.PositiveBigIntegerField(null=True)),
                ('age', models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(19)])),
                ('sex', models.PositiveBigIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True)),
                ('prediction', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
