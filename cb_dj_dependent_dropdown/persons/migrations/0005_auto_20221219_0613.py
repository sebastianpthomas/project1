# Generated by Django 3.2.16 on 2022-12-19 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_alter_person_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='DOB',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth(yy-mm-dd)'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Email',
            field=models.CharField(max_length=250),
        ),
    ]