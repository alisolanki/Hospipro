# Generated by Django 2.2.5 on 2019-10-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_patient_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
        ),
    ]
