# Generated by Django 3.1.2 on 2020-11-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201101_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='album_art',
            field=models.CharField(default='', max_length=254),
        ),
    ]
