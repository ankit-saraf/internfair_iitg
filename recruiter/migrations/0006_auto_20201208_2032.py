# Generated by Django 3.1.2 on 2020-12-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0005_auto_20201208_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internapplication',
            name='Status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('SHORTLISTED', 'shortlisted'), ('REJECTED', 'rejected')], default='PENDING', max_length=20),
        ),
    ]
