# Generated by Django 3.1.7 on 2022-07-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0012_activity_used_internal_conversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='internal_conversion_metric',
            field=models.FloatField(default=0),
        ),
    ]