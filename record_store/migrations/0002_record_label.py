# Generated by Django 3.1.2 on 2020-11-01 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='label',
            field=models.CharField(default='', max_length=254),
        ),
    ]
