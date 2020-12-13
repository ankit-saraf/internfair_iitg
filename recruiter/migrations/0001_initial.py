# Generated by Django 3.0.8 on 2020-12-13 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('internfair', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(blank=True, max_length=50)),
                ('stipend', models.IntegerField(blank=True)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('allowances', models.CharField(blank=True, max_length=150)),
                ('questions', models.TextField(max_length=200)),
                ('FormStatus', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE')], default='ACTIVE', max_length=10)),
                ('remarks', models.CharField(default='.', max_length=200)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intern_details', to='internfair.StartUps')),
            ],
        ),
        migrations.CreateModel(
            name='InternApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('PENDING', 'pending'), ('SHORTLISTED', 'shortlisted'), ('REJECTED', 'rejected')], default='PENDING', max_length=20)),
                ('Answers', models.TextField(max_length=400)),
                ('CV', models.CharField(default='not submitted', max_length=500)),
                ('Intern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internfair.Students')),
                ('Internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.Intern_form')),
            ],
        ),
    ]
