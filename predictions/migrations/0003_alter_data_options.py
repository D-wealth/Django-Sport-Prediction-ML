# Generated by Django 3.2.6 on 2022-04-08 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0002_data_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['-date']},
        ),
    ]
