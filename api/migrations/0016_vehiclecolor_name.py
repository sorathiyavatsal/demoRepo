# Generated by Django 3.1.7 on 2021-04-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210417_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclecolor',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
