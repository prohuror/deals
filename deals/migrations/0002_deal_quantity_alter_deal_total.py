# Generated by Django 4.0.1 on 2022-01-23 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='deal',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]