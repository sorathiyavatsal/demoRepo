# Generated by Django 3.1.7 on 2021-07-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_auto_20210722_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venderdetails',
            name='authorization_form',
            field=models.TextField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='venderdetails',
            name='background_check',
            field=models.TextField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='venderdetails',
            name='driver_licence_back',
            field=models.TextField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='venderdetails',
            name='driver_licence_front',
            field=models.TextField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='venderdetails',
            name='reg_insurence',
            field=models.TextField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='venderdetails',
            name='w9_form',
            field=models.TextField(blank=True, max_length=1000000, null=True),
        ),
    ]
