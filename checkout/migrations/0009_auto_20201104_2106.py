# Generated by Django 3.1.2 on 2020-11-04 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20201031_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order'),
        ),
    ]
