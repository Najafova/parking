# Generated by Django 2.2.3 on 2019-10-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkplace', '0015_auto_20191018_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='device_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]