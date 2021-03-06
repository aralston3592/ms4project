# Generated by Django 3.1.2 on 2020-11-01 17:54

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('artist', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=254)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=25)),
                ('track_listing', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=3600, size=50)),
                ('description', models.TextField(max_length=500)),
                ('album_art', models.CharField(default='', max_length=254)),
            ],
        ),
    ]
