# Generated by Django 3.0.3 on 2020-04-11 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postoffice', '0018_auto_20200411_0226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package_history',
            old_name='current_location_id',
            new_name='address',
        ),
    ]
