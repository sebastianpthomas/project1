# Generated by Django 3.2.16 on 2022-12-16 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20221216_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='geeks_field',
            new_name='DOB',
        ),
    ]
