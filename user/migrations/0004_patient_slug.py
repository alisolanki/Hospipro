# Generated by Django 2.2.5 on 2019-10-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20191002_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='slug',
            field=models.SlugField(default=2, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
