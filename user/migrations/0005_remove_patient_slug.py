# Generated by Django 2.2.5 on 2019-10-02 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_patient_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='slug',
        ),
    ]
