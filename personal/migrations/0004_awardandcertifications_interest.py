# Generated by Django 3.0.8 on 2020-08-07 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_skills_skillset'),
    ]

    operations = [
        migrations.CreateModel(
            name='awardandcertifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('link', models.URLField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
            ],
        ),
    ]
