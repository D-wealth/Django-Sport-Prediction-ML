# Generated by Django 3.2.6 on 2022-04-08 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0003_alter_data_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='prediction',
            new_name='predictions',
        ),
    ]