# Generated by Django 3.1.7 on 2021-05-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_remove_patient_test3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='test4',
            new_name='test_4',
        ),
        migrations.AddField(
            model_name='patient',
            name='test_3',
            field=models.ImageField(blank=True, null=True, upload_to='testphotos/test3'),
        ),
    ]
