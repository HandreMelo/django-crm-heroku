# Generated by Django 3.0.7 on 2020-08-14 00:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(default="", max_length=30),
            preserve_default=False,
        ),
    ]