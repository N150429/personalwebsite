# Generated by Django 3.0.8 on 2020-08-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_worksamples'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
