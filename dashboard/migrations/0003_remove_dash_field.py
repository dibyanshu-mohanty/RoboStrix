# Generated by Django 3.2 on 2021-05-01 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_dashadmin_dash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dash',
            name='field',
        ),
    ]
