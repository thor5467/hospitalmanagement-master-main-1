# Generated by Django 3.1.7 on 2021-05-27 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='test3',
        ),
    ]
