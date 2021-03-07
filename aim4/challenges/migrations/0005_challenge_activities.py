# Generated by Django 3.1.7 on 2021-03-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
        ('challenges', '0004_auto_20210307_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='activities',
            field=models.ManyToManyField(related_name='activities', through='challenges.Contribution', to='activities.Activity'),
        ),
    ]