# Generated by Django 3.0.2 on 2020-11-24 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_workout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]