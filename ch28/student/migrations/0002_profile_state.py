# Generated by Django 5.2.2 on 2025-06-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='kotli', max_length=100),
            preserve_default=False,
        ),
    ]
