# Generated by Django 4.2.9 on 2024-01-14 01:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_aichat_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aichat',
            name='content',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, null=True, size=None),
        ),
    ]