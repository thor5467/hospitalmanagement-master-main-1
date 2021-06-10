# Generated by Django 3.0.5 on 2021-06-10 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('appointmentDate', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('symptoms', models.CharField(max_length=100)),
                ('assignedDoctorId', models.PositiveIntegerField(null=True)),
                ('admitDate', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('Patient_type_1', models.CharField(choices=[('pretreatment', 'pretreatment'), ('Registrationcount', 'Registrationcount'), ('Preauthorisation', 'Preauthorisation'), ('Dischargestate', 'Dischargestate'), ('Claimphase', 'Claimphase'), ('surgery_update', 'surgery_update')], max_length=50)),
                ('status1', models.CharField(choices=[('approved', 'approved'), ('pending', 'pending'), ('approvedExcept', 'approvedExcept'), ('other', 'other'), ('caseStartedWithoutApproval', 'caseStartedWithoutApproval'), ('Running', 'Running'), ('compleated', 'compleated'), ('DischargeUpdated', 'DischargeUpdated'), ('DischargeUpdatePending', 'DischargeUpdatePending'), ('needToApply', 'needToApply'), ('claimApplied', 'claimApplied'), ('claimPending', 'claimPending'), ('claimapproved', 'claimapproved')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PatientDischargeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40)),
                ('assignedDoctorName', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('symptoms', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/dicharge/')),
                ('admitDate', models.DateField()),
                ('releaseDate', models.DateField()),
                ('daySpent', models.PositiveIntegerField()),
                ('roomCharge', models.PositiveIntegerField()),
                ('medicineCost', models.PositiveIntegerField()),
                ('doctorFee', models.PositiveIntegerField()),
                ('OtherCharge', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='test4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ImageField(blank=True, null=True, upload_to='testphotos/test4/')),
                ('discription', models.CharField(max_length=100)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='test3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ImageField(blank=True, null=True, upload_to='testphotos/test3/')),
                ('discription', models.CharField(max_length=100)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='test2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ImageField(blank=True, null=True, upload_to='testphotos/test2/')),
                ('discription', models.CharField(max_length=100)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ImageField(blank=True, null=True, upload_to='testphotos/test1/')),
                ('discription', models.CharField(max_length=100)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50)),
                ('status', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
